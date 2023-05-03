from pyswip import Prolog

prolog = Prolog()
prolog.consult("knowledge_base.pl")
END_FACTS = ":-"


def show_symptoms():
    my_list = [my_dict["X"]
               for my_dict in prolog.query("symptom(X, _)")]
    return [*set(my_list)]


def show_signs():
    my_list = [my_dict["X"]
               for my_dict in prolog.query("sign(X, _)")]
    return [*set(my_list)]


def show_tests():
    my_list = [my_dict["X"]
               for my_dict in prolog.query("test(X, _)")]
    return [*set(my_list)]


def show_medicines():
    my_list = [my_dict["X"]
               for my_dict in prolog.query("treatment(X, _)")]
    return [*set(my_list)]


def show_diseases():
    my_list = [my_dict["X"]
               for my_dict in prolog.query("symptom(_, X)")]
    my_list += [my_dict["X"]
               for my_dict in prolog.query("test(_, X)")]
    return [*set(my_list)]


def is_fact(fact: str):
    """
    Examples:\n
    "symptom(debilidad,ebola)"\n
    "sign(tos,coronavirus)."\n
    "test(examen_de_sangre,sifilis)"\n
    "treatment(lumefantrina,malaria)"
    """

    fact = fact.replace(" ", "")

    with open("test.pl", "r") as file:  # Read mode
        lines = file.readlines()

    if f"{fact}.\n" in lines:
        return True
    else:
        return False


def add_fact(fact: str):
    """
    Examples:\n
    "symptom(debilidad,ebola)"\n
    "sign(tos,coronavirus)."\n
    "test(examen_de_sangre,sifilis)"\n
    "treatment(lumefantrina,malaria)"
    """

    fact = fact.replace(" ", "")
    relation = fact.split("(")[0]

    with open("test.pl", "r") as file:  # Read mode
        lines = file.readlines()

    with open("test.pl", "w") as file:  # Write mode
        for number, line in enumerate(lines):
            if END_FACTS in line:
                break

            if relation in line:
                lines.insert(number, f"{fact}.\n")
                break

        file.writelines(lines)


def delete_fact(fact: str):
    """
    Examples:\n
    "symptom(debilidad,ebola)"\n
    "sign(tos,coronavirus)."\n
    "test(examen_de_sangre,sifilis)"\n
    "treatment(lumefantrina,malaria)"
    """

    fact = fact.replace(" ", "")

    with open("test.pl", "r") as file:  # Read mode
        lines = file.readlines()

    with open("test.pl", "w") as file:  # Write mode
        if is_fact(fact):
            lines.remove(f"{fact}.\n")
            file.writelines(lines)
