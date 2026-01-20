from pyscript import display, document

def results(e):
    reg = document.querySelector('input[name="reg"]:checked').value #Got this code from you ma'am
    med = document.querySelector('input[name="med"]:checked').value 
    grade = int(document.getElementById('grade').value)
    section = int(document.getElementById('section').value)

    if reg == "yes":
        if med == "yes":
            if section == 0:
               if grade == 0 or grade == 3:
                 display("Yeah! You are Red Bulldogs!", target = "output", append= False) #For some reason I can't make this show up even with the other ifs and elifs

            elif section == 1: 
                if grade == 1 or grade == 3:
                    display("Yeah! You are Green Hornets!", target ="output", append= False)

            elif section == 2: 
                if grade == 2 or grade == 3:
                    display("Yeah! You are Yellow Tigers!", target ="output", append= False)

            elif section == 3: 
                if grade == 0 or grade == 3:
                    display("Yeah! You are Blue Bears!", target ="output", append= False)

            elif section == 4: 
                if grade == 2 or grade == 1:
                    display("Yeah! You are Green Hornets!", target ="output", append= False)
        else:
            display("Please have a letter from the clinic", target ="output", append= False) #To show that the person lacks a med letter from the clinic
    else:
            display("Please register or tell your PE teacher before joining in the Intrams", target ="output", append= False) #to show that the person that they can't join if they haven't regester
            #My else works unlike my ifs and elifs
                
          

        
