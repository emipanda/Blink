# Blink Ops - Assignment

The json of the form should be like that:
[   
    {
        "id": 0, // number counting from 0
        "question" : "Burger/Pizza?", // String of question
        "type": "single_choice", // [single_choice / multi_choice / int / open ]
        "answers": {"Burger": 1, "Pizza": 2} // if single_choice or multi_choice -> {$answer: $follow_up_number}
    },
  {
        "id": 1,
        "question" : "MW/M/WD?",
        "type": "single_choice",
        "answers": {"MW": 4, "M": 4, "WD": 4}
    },
    {
        "id": 2,
        "question" : "Choose your toppings: [onion, tomato, mushrooms]",
        "type": "multi_choice",
        "answers": {"onion": 3, "tomato": 3, "mushrooms": 3}
    },
    {
        "id": 3,
        "question" : "How many pizzaz like that would you like?",
        "type": "int", 
        "next_question": -1 // if int then add next_question field and if it the last question put -1
    }
]
