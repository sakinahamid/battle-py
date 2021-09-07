__author__ = "Sakinah Abdul Hamid"

from army import Army

class Battle:

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """ Creates army for each player, sets them in stack formation, and calls
        internal method __conduct_combat().

        :complexity: Best and worst O(Comp_choose_army() + Comp__conduct_combat()), where Comp_choose_army()
        is the complexity of choose_army() and Comp__conduct_combat() is the complexity of __conduct_combat().
        """

        army1 = Army()
        army1.choose_army(player_one, 0)
        army2 = Army()
        army2.choose_army(player_two, 0)

        return self.__conduct_combat(army1, army2, 0)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """ Creates army for each player, sets them in queue formation, and calls
        internal method __conduct_combat().

        :complexity: Best and worst O(Comp_choose_army() + Comp__conduct_combat()), where Comp_choose_army()
        is the complexity of choose_army() and Comp__conduct_combat() is the complexity of __conduct_combat().
        """

        army1 = Army()
        army1.choose_army(player_one, 1)
        army2 = Army()
        army2.choose_army(player_two, 1)

        return self.__conduct_combat(army1, army2, 1)

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """ Conducts a battle between these two armies following a method that depends on the formation.

        :complexity: Best and worst O((min(n1, n2))), where n1 and n2 are the lengths of army1 and army2 respectively.
        """

        if formation == 0:

            while (not army1.force.is_empty()) and (not army2.force.is_empty()):
                #pop a fighter each from army1 and army2
                u1 = army1.force.pop()
                u2 = army2.force.pop()

                while u1.is_alive() and u2.is_alive():
                    self.__attack_defend(u1, u2)

                    #aftermath of attack/defend
                    if u1.is_alive() and u2.is_alive(): #when both u1 and u2 is alive
                        u1.lose_life(1)
                        u2.lose_life(1)
                    elif u1.is_alive(): #when only u1 is alive
                        u1.gain_experience(1)
                        army1.force.push(u1)
                    elif u2.is_alive(): #when only u2 is alive
                        u2.gain_experience(1)
                        army2.force.push(u2)
                    # if u1 and u2 does not survive (else), the loop breaks

        elif formation == 1:

            while (not army1.force.is_empty()) and (not army2.force.is_empty()):

                #serve a fighter each from army1 and army2
                u1 = army1.force.serve()
                u2 = army2.force.serve()

                while u1.is_alive() and u2.is_alive():

                    self.__attack_defend(u1, u2)

                    #aftermath of attack/defend
                    if u1.is_alive() and u2.is_alive():  # when both u1 and u2 is alive
                        u1.lose_life(1)
                        u2.lose_life(1)
                    elif u1.is_alive():  # when only u1 is alive
                        u1.gain_experience(1)
                        army1.force.append(u1)
                    elif u2.is_alive():  # when only u2 is alive
                        u2.gain_experience(1)
                        army2.force.append(u2)
                    # if u1 and u2 does not survive (else), the loop breaks

        return self.__battle_champion(army1, army2)

    def __attack_defend(self, u1: Army, u2: Army) -> None:
        """ Initiates the attack/defend stage of the battle (based on the information given in the 'Background'
        section of Interview Prac 2.)

        :complexity: Best and worst O(1), as:
                     - Comp_get_speed() is O(1)
                     - Comp_attack_damage() is O(1)
                     - Comp_defend() is O(1)
                     - Comp_is_alive() is O(1)
                     - assignments are always constant
                     - integer comparisons are always constant
                     - boolean comparisons are always constant
        """

        # attack/defend stage (based on Background)
        if u1.get_speed() > u2.get_speed():
            d1 = u1.attack_damage()
            u2.defend(d1)
            if u2.is_alive():  # if u2 dies after the attack before, u1 will not take any damage
                d2 = u2.attack_damage()
                u1.defend(d2)
        elif u2.get_speed() > u1.get_speed():
            d2 = u2.attack_damage()
            u1.defend(d2)
            if u1.is_alive():  # if u1 dies after the attack before, u2 will not take any damage
                d1 = u1.attack_damage()
                u2.defend(d1)
        elif u1.get_speed() == u2.get_speed:
            d1 = u1.attack_damage()
            d2 = u2.attack_damage()
            u1.defend(d2)
            u2.defend(d1)

    def __battle_champion(self, army1: Army, army2: Army) -> int:
        """ Once the battle is over, the result of the battle will be decided

        :complexity: Best and worst case is O(1), as boolean comparisons and return statements are
        always constant, and Comp_is_empty() is O(1).
        """

        if army1.force.is_empty() and army2.force.is_empty():
            return 0  # draw
        elif army2.force.is_empty():
            return 1  # player_one wins
        elif army1.force.is_empty():
            return 2  # player_two wins

if __name__ == "__main__":
    test = Battle()
    print(test.gladiatorial_combat("James", "Robert"))
    # t1 = Army()
    # t2 = Army()
    # battle = Battle()
    # formation = 1
    # t1._Army__assign_army("", 1, 1, 1, formation)
    # t2._Army__assign_army("", 1, 1, 1, formation)
    # print(battle._Battle__conduct_combat(t1, t2, formation))
    # print("t1 = " + str(t1.force))
    # print("t2 = " + str(t2.force))
