%Facts
symptom(cansancio,anemia).
symptom(desnutricion,anemia).
symptom(tos,gripe).

test(fiebre,gripe).
test(dolor,gripe).

treatment(jarabe,tos).
treatment(paracetamol,fiebre).
treatment(vitaminas,cansancio).
treatment(xl3,gripe).

%Rules
sick(Patient, Disease) :- has_symptom(Patient, Symptom), symptom(Symptom, Disease).
sick(Patient, Disease) :- has_test(Patient, Test), test(Test, Disease).

prescribe(Medicine, _, Disease) :- treatment(Medicine, Disease).
prescribe(Medicine, Patient, _) :- treatment(Medicine, Symptom), has_symptom(Patient, Symptom).
prescribe(Medicine, Patient, _) :- treatment(Medicine, Test), has_test(Patient, Test).
