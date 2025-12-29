import random
import os


class Team:
    def __init__(self):
        self.team_names = [
            "Олександр",
            "Дмитро",
            "Сергій",
            "Андрій",
            "Максим",
            "Іван",
            "Артем",
            "Михайло",
            "Кирило",
            "Владислав",
            "Єгор",
            "Роман",
            "Денис",
            "Тимур",
            "Олег"
        ]

    def show_team_member(self):
        num_list = 1
        num_team = 5
        print(f"Твої член команди:\n")
        while num_team > 0:
            member = random.choice(self.team_names)
            print(f"{num_list} - {member}")


            self.team_names.remove(member)
            self.in_team = self.team_names.append(member)
            num_team = num_team - 1
            num_list += 1






class Menu:
    def __init__(self, team_list):
        self.in_team

    def menu(self):
        print("Можем позвати команду? - 1 це так")
        choice = int(input())
        if choice == 1:
            print(f'твоя вся команда: {self.in_team}')
        else:
            print('пупупу')

class Start:
    def __init__(self):
        self.captain_name = ""

    def start(self):
        with open(os.getcwd() + "\\boat.txt", "r", encoding="utf-8") as file:
            content = file.read()


        print(
            f"{content}\nГра boat — це гра про підводну лодку і про те як нею управляти\n"
            "Ти капітан!\n"
            "Пора назвати себе:"
        )
        self.captain_name = input()
        print(f"Чудове ім'я, капітане {self.captain_name}")

        team = Team()
        team.show_team_member()
        full_team = Menu()
        full_team.menu()

if __name__ == "__main__":
    game = Start()
    game.start()
