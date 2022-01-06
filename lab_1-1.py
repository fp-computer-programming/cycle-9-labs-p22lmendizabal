#author: LM (AMDG) 1/6/22
def create_possesive(rows):
    for lst in rows:
        for name in lst:
            if name[-1] == "s":
                name = name + "'"
            else:
                name= name +"'s"

            print(name)

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin", "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

create_possesive(rows)