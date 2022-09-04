from os.path import exists, basename
import json
from this import d

forms = {}

def main():
    exit_program = False
    while not exit_program:
        choice = input("Please, choose an action:\n "
                       "1. Import a form \n "
                       "2. Fill in a form \n ")
        if choice == "1":
            import_form()
        elif int(choice) == 2:
            fill_form()
        else:
            print("Wrong input, try again")


def import_form():
    path = input("Enter the form path:\n")
    while not exists(path):
        path = input("The file doesn't exist, please enter path again:\n")
    print("Form imported successfully!\n")
    with open(path) as f:
        parsed_json = json.load(f)
    form_name = basename(path).rsplit('.', maxsplit=1)[0]
    forms[form_name] = parsed_json


def process_question(form_json, question_id, response_json):
    if (question_id == -1):
        return
    # follow up quistions
    for question in form_json:
        if question["id"] == question_id:
            picked_item = question
            break
    valid_answer = False
    answer = ''
    question_type = picked_item['type'] if 'type' in picked_item.keys() else 'open'
    acceptable_answers = []
    if 'answers' in picked_item.keys():
        acceptable_answers = picked_item['answers']

    #single choice case
    if (question_type == "single_choice"):
        while not valid_answer:
            answer = input(picked_item['question'] + "\n")
            if (answer in picked_item['answers'].keys()):
                valid_answer = True
            else:
                print("Wrong input")
        response_json[picked_item['question']] = answer
        process_question(form_json, picked_item['answers'][answer], response_json)
    
    #multi choice case
    elif (question_type == "multi_choice"):
        while not valid_answer:
            answer = input(picked_item['question'] + "\n")
            split_answer = answer.split(',')
            valid_answer = True
            for a in split_answer:
                if a.strip() not in acceptable_answers.keys():
                    valid_answer = False
                    print('Wrong input')
                    break
            response_json[picked_item['question']] = answer
            process_question(form_json, picked_item["answers"][split_answer[0]], response_json)

    #Integer answer case
    elif (question_type == "int"):
        while not valid_answer:
            answer = input(picked_item['question'] + "\n")
            valid_answer = answer == str(int(answer))
        
        response_json[picked_item['question']] = answer
        process_question(form_json, picked_item["next_question"], response_json)
    
    #Open answer case
    elif(question_type == "open"): 
        answer = input(picked_item['question'] + "\n") 
        response_json[picked_item['question']] = answer

        
def fill_form():
    str_input = "Choose a form:"
    for i, form in enumerate(forms.keys()):
        str_input += f"\n{i+1}. {form}\n"

    form_choice = input(str_input)
    form_name = list(forms.keys())[int(form_choice)-1]
    
    response_json = {}
    process_question(forms[form_name], 0, response_json)
    export_form(response_json)


def export_form(response_json):
    print("Thank you for filling the form, here it is:")
    print(response_json)
    with open(".\out.json", "w") as outfile:
        json.dump(response_json, outfile)
    

if __name__ == "__main__":
    main()
