__author__ = "Sakinah Abdul Hamid"

from abc import ABC, abstractmethod
from stack import ArrayStack
from FITQueue import CircularQueue


class Fighter(ABC):
    def __init__(self, life: int, experience: int) -> None:
        """ Appropriately initialises the variables using the amounts received as input.

        :pre: life & experience >= 0
        :raises Exception: if life & experience < 0
        :complexity: Best and worst O(1), as integer comparisons are always constant and
         assignments are always constant.
        """
        if life < 0 and experience < 0:
            raise Exception("life & experience must be >= 0")
        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:
        """Returns True if the fighter’s life is greater than 0, False otherwise.

        :complexity: Best and worst O(1), as integer comparisons are always constant and
        return statements are always constant.
        """
        return self.life > 0

    def lose_life(self, lost_life: int) -> None:
        """Decreases the life of the unit by the amount indicated by lost_life.

        :pre: lost_life >= 0
        :raises Exception: if lost_life < 0
        :complexity: Best and worst O(1), as integer comparisons, basic numerical operations and
        assignments are always constant.
        """
        if lost_life < 0:
            raise Exception("lost_life must be >= 0")
        self.life -= lost_life

    def gain_experience(self, gained_experience: int) -> None:
        """ Increases the experience of the unit by the amount indicated by gained_experience.

        :pre: gained_experience must be >= 0
        :raises Exception: if gained_experience < 0
        :complexity: Best and worst O(1), as integer comparisons, basic numerical operations and
        assignments are always constant.
        """
        if gained_experience < 0:
            raise Exception("gained_experience must be >= 0")
        self.experience += gained_experience

    def get_experience(self) -> int:
        """ Returns the experience of the unit."""
        return self.experience

    @abstractmethod
    def get_speed(self) -> int:
        """Returns the speed of the unit. """
        pass

    @abstractmethod
    def get_cost(self) -> int:
        """ Returns the cost of the unit. """
        pass

    @abstractmethod
    def attack_damage(self) -> int:
        """ Returns the amount of damage performed by the unit when it attacks."""
        pass

    @abstractmethod
    def defend(self, damage: int) -> None:
        """  Decreases the life indicated by damage.

        :pre: damage must be >= 0
        :raises Exception: if gained_experience < 0
        """
        if damage < 0:
            raise Exception("damage must be >= 0")
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Returns a string indicating the type of unit, its current life and experience."""
        pass


class Soldier(Fighter):
    def __init__(self) -> None:
        """ Appropriately initialises the variables using the amounts received as input.

        :complexity: Best and worst O(1), since assignments are always constant and Fighter.__init()'s
        complexity is O(1).
        """
        Fighter.__init__(self, 3, 0)
        self.speed = 0
        self.cost = 1

    def get_speed(self) -> int:
        """Returns the speed of the unit.

        :complexity: Best and worst O(1), as assignments, basic numerical operations and return
        statements are always constant.
        """
        self.speed = 1 + self.experience
        return self.speed

    def get_cost(self) -> int:
        """ Returns the cost of the unit.

        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return self.cost

    def attack_damage(self) -> int:
        """ Returns the amount of damage performed by the unit when it attacks.

        :complexity: Best and worst O(1), as return statements and basic numerical operations
         are always constant.
        """
        return 1 + self.experience

    def defend(self, damage: int) -> None:
        """  Decreases the life indicated by damage.

        :complexity: Best and worst O(1), as integer comparisons, basic numerical operations
         and assignments are always constant.
        """
        if damage > self.experience:
            self.life -= 1

    def __str__(self) -> str:
        """ Returns a string indicating the type of unit, its current life and experience.

        :format: "Soldier’s life = X and experience = Y"
        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return "Soldier's life = " + str(self.life) + " and experience = " + str(self.experience)


class Archer(Fighter):
    def __init__(self) -> None:
        """Appropriately initialises the variables using the amounts received as input.

        :complexity: Best and worst O(1), since assignments are always constant and Fighter.__init()'s
        complexity is O(1).
        """
        Fighter.__init__(self, 3, 0)
        self.speed = 3
        self.cost = 2

    def get_speed(self) -> int:
        """Returns the speed of the unit.

        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return self.speed

    def get_cost(self) -> int:
        """ Returns the cost of the unit.

        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return self.cost

    def attack_damage(self) -> int:
        """ Returns the amount of damage performed by the unit when it attacks.

        :complexity: Best and worst O(1), as return statements and basic numerical operations
        are always constant.
        """
        return 1 + self.experience

    def defend(self, damage: int) -> None:
        """  Decreases the life indicated by damage."""
        self.life -= 1

    def __str__(self) -> str:
        """ Returns a string indicating the type of unit, its current life and experience.

        :format: "Archer’s life = X and experience = Y"
        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return "Archer's life = " + str(self.life) + " and experience = " + str(self.experience)


class Cavalry(Fighter):
    def __init__(self) -> None:
        """Appropriately initialises the variables using the amounts received as input.

        :complexity: Best and worst O(1), since assignments are always constant and Fighter.__init()'s
        complexity is O(1).
        """
        Fighter.__init__(self, 4, 0)
        self.speed = 2
        self.cost = 3

    def get_speed(self) -> int:
        """Returns the speed of the unit.

        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return self.speed

    def get_cost(self) -> int:
        """ Returns the cost of the unit.

        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return self.cost

    def attack_damage(self) -> int:
        """ Returns the amount of damage performed by the unit when it attacks.

        :complexity: Best and worst O(1), as return statements and basic numerical operations
        are always constant.
        """
        return (2 * self.experience) + 1

    def defend(self, damage: int) -> None:
        """  Decreases the life indicated by damage.

        :complexity: Best and worst O(1), as integer comparisons, basic numerical operations
         and return statements are always constant.
        """
        if damage > (self.experience / 2):
            self.life -= 1

    def __str__(self) -> str:
        """ Returns a string indicating the type of unit, its current life and experience.

        :format: "Cavalry’s life = X and experience = Y"
        :complexity: Best and worst O(1), as return statements are always constant.
        """
        return "Cavalry's life = " + str(self.life) + " and experience = " + str(self.experience)


class Army():
    def __init__(self) -> None:
        """ Appropriately initialises the variables using to None."""
        self.name = None
        self.force = None

    def choose_army(self, name: str, formation: int) -> None:
        """ Creates a loop that asks input (s, a, c) from user, checks if the user input is valid, then sets
        up the army according to the formation. Else, it asks for user input up until it meets the conditions.

        :raises IndexError: if the input less than/more than 3 inputs
        :raises ValueError: if the input is a string
        :complexity: N * (M + CompSplit + temp + Comp__assign_army()) which gives the complexity of O(N *
        (M + CompSplit + temp + Comp__assign_army()) where:
                     - N is the number of times user gives an input
                     - M is the length of the string "statement"
                     - CompSplit is the complexity of split()
                     - temp is the length of list temp
                     - Comp__assign_army() is the complexity of __assign_army().
        It will always be executed O(N * (M + CompSplit + temp + Comp__assign_army()) times, so best case = worse case.
        """
        correct_input = False

        while not correct_input:
            try:
                statement = "Player " + name + " choose your army as S A C \nwhere  S is the number of soldiers \n       A is the number of archers \n       C is the number of cavalry"
                print(statement)
                temp = input().split()
                lst = []
                for i in temp:
                    lst.append(int(i))
                s = lst[0] #soldier
                a = lst[1] #archer
                c = lst[2] #cavalry

                if self.__correct_army_given(s, a, c):  # if the input is correct, __assign_army() will be called
                    correct_input = True
                    return self.__assign_army(name, s, a, c, formation)
                else:
                    raise ValueError

            except IndexError:
                print("You must give 3 inputs. Please try again (when you don't want to buy an army, please input 0).")

            except ValueError:
                print("The input you entered is invalid. Please try again.")

    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
        """ An internal method to ensure that the input given is valid.

        :complexity: Best and worst O(1), as return statements and integer comparisons
        are always constant.
        """

        b1 = soldiers >= 0
        b2 = archers >= 0
        b3 = cavalry >= 0
        b4 = soldiers + archers + cavalry <= 30

        if b1 & b2 & b3 & b4:
            return True
        return False

    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int) -> None:
        """ Forms the formation of army.

        :pre: formation can only be 0 (for stack) and 1 (for queue)
        :raises Exception: when formation is not 0 or 1
        :complexity: Best and worst O(sold + arch + cav), where sold is the number of soldiers
        bought, arch is the number of archers bought and cav is the number of cavalry bought. All loop
        (depending on the formation) will always be entered and run (sold + arch + cav) times as we are
        forming the stack/queue, so we will never have a full stack/queue to begin with.
        """
        total = sold + arch + cav

        if formation == 0:

            adt = ArrayStack(total)
            if not adt.is_full():
                for i in range(cav):
                    c = Cavalry()
                    adt.push(c)
                for i in range(arch):
                    a = Archer()
                    adt.push(a)
                for i in range(sold):
                    s = Soldier()
                    adt.push(s)

        elif formation == 1:
            adt = CircularQueue(total)
            if not adt.is_full():
                for i in range(sold):
                    s = Soldier()
                    adt.append(s)
                for i in range(arch):
                    a = Archer()
                    adt.append(a)
                for i in range(cav):
                    c = Cavalry()
                    adt.append(c)

        else:
            raise Exception("Input number for formation is invalid.")
        self.force = adt
        self.name = name

    def __str__(self) -> str:
        """ Returns a string indicating the type of unit(n), its current life and experience.

        :format: "n’s life = X and experience = Y"
        :complexity: Best and worst O(1), as return statements are always constant and __str()
        of Fighter method is O(1).
        """
        return str(self.force)

if __name__ == "__main__":
    test = Army()
    test.choose_army("Max", 1)
    print(str(test))











