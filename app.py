from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

dog_breeds = [
    {
        "breed": "Shiba Inu",
        "origin": "Japan",
        "size": "Medium",
        "personality": "Alert, agile, and good-natured",
        "fun_fact": "They're known for the 'Shiba scream' - a distinctive vocalization when excited or upset",
        "care_tip": "They're very clean dogs and groom themselves like cats",
        "energy_level": "High",
        "good_for": "Experienced owners who appreciate independence"
    },
    {
        "breed": "Xoloitzcuintli",
        "origin": "Mexico",
        "size": "Varies (toy to standard)",
        "personality": "Calm, loyal, and alert",
        "fun_fact": "This hairless breed is over 3,000 years old and was considered sacred by the Aztecs",
        "care_tip": "Their skin needs sunscreen and moisturizer like humans",
        "energy_level": "Moderate",
        "good_for": "People with allergies seeking a unique companion"
    },
    {
        "breed": "Norwegian Lundehund",
        "origin": "Norway",
        "size": "Small to Medium",
        "personality": "Energetic, loyal, and alert",
        "fun_fact": "They have 6 toes on each foot and can close their ears by folding them shut",
        "care_tip": "They need mental stimulation due to their problem-solving heritage",
        "energy_level": "Very High",
        "good_for": "Active families who love hiking"
    },
    {
        "breed": "Azawakh",
        "origin": "West Africa",
        "size": "Large",
        "personality": "Independent, loyal, and gentle",
        "fun_fact": "They can reach speeds up to 40 mph and are excellent guard dogs",
        "care_tip": "They're sensitive to cold and need warm clothing in winter",
        "energy_level": "High",
        "good_for": "Experienced owners with secure yards"
    },
    {
        "breed": "Telomian",
        "origin": "Malaysia",
        "size": "Medium",
        "personality": "Intelligent, adaptable, and friendly",
        "fun_fact": "They were originally bred to climb ladders in Malaysian villages",
        "care_tip": "They're excellent climbers and need secure, tall fencing",
        "energy_level": "High",
        "good_for": "Active families who enjoy training challenges"
    },
    {
        "breed": "Mudi",
        "origin": "Hungary",
        "size": "Medium",
        "personality": "Versatile, intelligent, and active",
        "fun_fact": "They're one of the rarest herding breeds and excel at multiple dog sports",
        "care_tip": "They need a job to do - mental stimulation is crucial",
        "energy_level": "Very High",
        "good_for": "Farmers or very active families"
    },
    {
        "breed": "Kai Ken",
        "origin": "Japan",
        "size": "Medium",
        "personality": "Brave, intelligent, and loyal",
        "fun_fact": "Their brindle coat changes color as they age, and they're excellent climbers",
        "care_tip": "They're naturally clean and rarely need baths",
        "energy_level": "High",
        "good_for": "Experienced owners who want a devoted companion"
    },
    {
        "breed": "Lagotto Romagnolo",
        "origin": "Italy",
        "size": "Medium",
        "personality": "Affectionate, keen, and undemanding",
        "fun_fact": "They're the only breed specifically bred to hunt truffles",
        "care_tip": "Their curly coat needs regular grooming to prevent matting",
        "energy_level": "Moderate to High",
        "good_for": "Families who want a unique, intelligent pet"
    }
]

@app.route('/dog-breed-generator', methods=['GET'])
def get_dog_breed():
    selected_breed = random.choice(dog_breeds)
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    
    response = {
        "date": current_date,
        "time": current_time,
        "generated_breed": selected_breed["breed"],
        "breed_details": {
            "origin": selected_breed["origin"],
            "size": selected_breed["size"],
            "personality": selected_breed["personality"],
            "energy_level": selected_breed["energy_level"],
            "good_for": selected_breed["good_for"]
        },
        "fun_fact": selected_breed["fun_fact"],
        "care_tip": selected_breed["care_tip"],
        "message": f"Generated breed: {selected_breed['breed']}! 🐕",
        "api_info": "Dog Breed Generator API v1.0"
    }
    
    return jsonify(response)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Dog Breed Generator API!",
        "endpoint": "/dog-breed-generator",
        "description": "Generate information about unique dog breeds",
        "creator": "IT SIA31 Student",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)