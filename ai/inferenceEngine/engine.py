from pyswip import Prolog

prolog = Prolog()
prolog.consult("ai/inferenceEngine/knowledge_base.pl")


def most_frequent(my_list):
        return max(set(my_list), key=my_list.count)

def diagnose(conditions: list, queue):
    # Temporarily add patient's symptoms, signs and tests
    for condition in conditions:
        prolog.assertz(f"has({condition})")

    # Show probable diseases
    diseases = [my_dict["X"]
                for my_dict in prolog.query(f"sick(X)")]

    # Choose one desease
    disease = most_frequent(diseases)

    # Prescribe medicine
    medicines = [my_dict["X"]
                 for my_dict in prolog.query(f"prescribe(X, {disease})")]

    # Return the desease and the medicines
    result = [disease]
    result.append(medicines)

    queue.put(result)
    
