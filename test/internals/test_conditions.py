from test.framework import FrameworkTestGame

class TestCondition(FrameworkTestGame):
    def test_addCondition(self):
        condition = Condition(CONDITION_FIRE, length=10, damage=1)
        self.player.condition(condition)

        self.assertTrue(self.player.conditions)
        self.assertTrue(condition.creature)

    def test_hascondition(self):
        condition = Condition(CONDITION_FIRE, length=10, damage=1)
        self.player.condition(condition)

        self.assertTrue(self.player.hasCondition(CONDITION_FIRE))

    def test_getcondition(self):
        condition = Condition(CONDITION_FIRE, length=10, damage=1)
        self.player.condition(condition)

        self.assertEqual(self.player.getCondition(CONDITION_FIRE), condition)