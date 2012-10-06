from .. import framework

class TestParty(framework.FrameworkTestGame):
    def test_create_party(self):
        # We have no party.
        self.assertFalse(self.player.party())
        
        # Make a new party
        party = self.player.newParty()
        
        self.assertTrue(party)
        self.assertEqual(party, self.player.party())
        self.assertIsInstance(party, game.party.Party)
        
        # We're leader?
        self.assertEqual(party.leader, self.player)
        
        # We're member?
        self.assertTrue(self.player in party.members)
        
        
    def test_disband_party(self):
        party = self.player.newParty()
        
        party.disband()
        
        self.assertFalse(self.player.party())
        
    def test_leave_party(self):
        party = self.player.newParty()
        
        self.player.leaveParty()
        
        self.assertFalse(self.player in party.members)
        
    def test_leave_party_disband(self):
        party = self.player.newParty()
        
        self.player.leaveParty()
        
        self.assertFalse(party.members)
        self.assertFalse(party.leader)
        
    def test_party_invite(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addInvite(member)
        
        self.assertTrue(member in party.invites)
        
        # Leaders shield?
        self.assertEqual(member.getShield(self.player), SHIELD_LEADER_INVITE)
        
        # Members shield?
        self.assertEqual(self.player.getShield(member), SHIELD_MEMBER_INVITE)
        
        # Only invite?
        self.assertEqual(len(party.invites), 1)
        
    def test_multiple_invites(self):
        partyLeader = self.setupPlayer()
        member = self.setupPlayer()
        
        party1 = partyLeader.newParty()
        party2 = self.player.newParty()
        
        party1.addInvite(member)
        party2.addInvite(member)
        
        self.assertTrue(member in party1.invites)
        self.assertTrue(member in party2.invites)
        
        # Leaders shield?
        self.assertEqual(member.getShield(self.player), SHIELD_LEADER_INVITE)
        self.assertEqual(member.getShield(partyLeader), SHIELD_LEADER_INVITE)
        
        # Members shield?
        self.assertEqual(self.player.getShield(member), SHIELD_MEMBER_INVITE)
        self.assertEqual(partyLeader.getShield(member), SHIELD_MEMBER_INVITE)
        
        # Only invite?
        self.assertEqual(len(party1.invites), 1)
        self.assertEqual(len(party2.invites), 1)
        
    def test_join(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addInvite(member)
        
        party.addMember(member)
        
        # Now invites should be empty
        self.assertFalse(party.invites)
        
        # And we'll be a member.
        self.assertTrue(member in party.members)
        
        # We should also have a party shield.
        self.assertEqual(member.getShield(self.player), SHIELD_MEMBER)
        
        # And leader a leader shield.
        self.assertEqual(self.player.getShield(member), SHIELD_LEADER)
        
        # And get the correct party object.
        self.assertEqual(party, member.party())
        
    def test_change_leader(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addMember(member)
        
        party.changeLeader(member)
        
        # We're leader?
        self.assertEqual(party.leader, member)
        
        # Old leader is member?
        self.assertTrue(self.player in party.members)
        
        # Shields are already tested...
        
    def test_leave_party(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addMember(member)
        
        party.removeMember(member)
            
        self.assertFalse(member in party.members)
        self.assertFalse(member.party())
        
    def test_leave_party_disband(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addMember(member)
        
        party.removeMember(member)
            
        self.assertFalse(party.members)
        self.assertFalse(party.leader)
        
    def test_leave_pass_leadership(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        member2 = self.setupPlayer()
        
        party.addMember(member)
        party.addMember(member2)
        
        # Leader leave.
        party.removeMember(self.player)
            
        # Member1 is new leader?
        self.assertEqual(member, party.leader)
        self.assertEqual(len(party.members), 2)
        
    def test_toggle_share_experience(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addMember(member)
        
        self.assertFalse(party.shareExperience)
        
        party.toggleShareExperience()
        
        self.assertTrue(party.shareExperience)
        
        # shields.
        self.assertEqual(member.getShield(self.player), SHIELD_MEMBER_SHAREDEXP)
        
        self.assertEqual(self.player.getShield(member), SHIELD_LEADER_SHAREDEXP)
        
    def test_toggle_not_ok_share_experience(self):
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addMember(member)
        
        # Set member level high.
        member.data["level"] = 10000
        
        party.toggleShareExperience()
        
        # shields.
        self.assertEqual(member.getShield(self.player), SHIELD_MEMBER_NOSHAREDEXP)
        
        self.assertEqual(self.player.getShield(member), SHIELD_LEADER_NOSHAREDEXP)
        
    def test_share_experience(self):
        # Turn of protection zone
        self.overrideConfig("protectedZones", False)
        
        party = self.player.newParty()
        
        member = self.setupPlayer()
        
        party.addMember(member)
        
        party.toggleShareExperience()

        # Make a monster
        bmonster = game.monster.genMonster("__TEST__", (0,0))
        bmonster.setExperience(100)
        bmonster.setHealth(1)
        
        # Spawn.
        monster = getMonster("__TEST__").spawn(self.player.positionInDirection(NORTH), spawnDelay=0, radius=0)
        monster.setRespawn(False)
        
        # old experience.
        member1Exp = self.player.data["experience"]
        member2Exp = member.data["experience"]
        
        # Attack.
        self.player.ignoreBlock = True
        self.player.target = monster
        self.player.targetMode = 1
        self.player.attackTarget(-100)
        
        # Check experience.
        self.assertGreater(self.player.data["experience"], member1Exp)
        self.assertGreater(member.data["experience"], member2Exp)
        
        # Check exact experience. It's 50.
        self.assertEqual(self.player.data["experience"], member1Exp+50)
        self.assertEqual(member.data["experience"], member2Exp+50)
        
        # Cleanups
        del game.monster.monsters["__TEST__"]
        self.restoreConfig("protectedZones")
        
        