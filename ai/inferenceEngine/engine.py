from pyswip import Prolog

prolog = Prolog()
prolog.consult("knowledge_base.pl")


def most_frequent(my_list):
        return max(set(my_list), key=my_list.count)

def diagnose(patient: str, symptoms: list = ["none"], tests: list = ["none"]):
    # Temporarily add patient's symptoms
    for symptom in symptoms:
        prolog.assertz(f"has_symptom({patient}, {symptom})")
    
    # Temporarily add patient's tests
    for test in tests:
        prolog.assertz(f"has_test({patient}, {test})")

    # Show probable diseases
    diseases = [my_dict["X"]
                for my_dict in prolog.query(f"sick({patient}, X)")]

    # Chose one desease
    disease = most_frequent(diseases)

    # Prescribe medicine
    medicines = [my_dict["X"]
                 for my_dict in prolog.query(f"prescribe(X, {patient}, {disease})")]

    # Return the desease and the medicines
    result = [disease]
    result.append(medicines)
    return result
print(diagnose("juan", ["dolor_de_torax"], ["test_ELISA"]))