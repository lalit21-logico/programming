class Member:
    def __init__(self, name):\
            # instance variable of Member class
        self.name = name

    def display(self):
        print(self.name)


class Team:
    def __init__(self, no_of_member, member):
        # instance variable of team class
        self.no_of_member = no_of_member
        self.member = member
        self.member_class_ob = Member(self.member)

    def display(self):
        Member.display(self.member_class_ob)


# creat insatnce of Team and call Team's display Method
Team.display(Team(10, "George"))
