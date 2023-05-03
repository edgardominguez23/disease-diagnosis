%Facts, soruce: https://cuidateplus.marca.com/enfermedades/infecciosas.html
symptom(cansancio,coronavirus).
symptom(perdida_del_olfato,coronavirus).
symptom(perdida_del_gusto,coronavirus).
symptom(dolor_de_garganta,coronavirus).
symptom(dolor_de_cabeza,coronavirus).
symptom(dificultad_para_respirar,coronavirus).
symptom(debilidad,ebola).
symptom(dolor_muscular,ebola).
symptom(dolor_de_cabeza,ebola).
symptom(dolor_de_garganta,ebola).
symptom(dolor_de_cabeza,ebola).
symptom(dolor_muscular,ebola).
symptom(dolor_de_articulaciones,ebola).
symptom(dolor_de_torax,ebola).
symptom(nauseas,ebola).
symptom(dolor_abdominal,ebola).
symptom(dolor_epigastrico,ebola).
symptom(perdida_de_la_sensibilidad,lepra).
symptom(dolor_de_cabeza,malaria).
symptom(dolor_muscular,malaria).
symptom(escalofrios,malaria).
symptom(escalofrios,peste).
symptom(dolor_de_cabeza,peste).
symptom(debilidad,peste).
symptom(nauseas,peste).
symptom(dolor_de_garganta,sifilis).
symptom(dolor_de_cabeza,sifilis).
symptom(dolor_muscular,sifilis).
symptom(cansancio,sifilis).
symptom(entumecimiento,sifilis).
symptom(demencia,sifilis).
symptom(ceguera,sifilis).
symptom(cansancio,tuberculosis).
symptom(malestar_general,tuberculosis).
symptom(dolor_de_garganta,difteria).
symptom(debilidad,difteria).
symptom(dificultad_para_respirar,difteria).

sign(tos,coronavirus).
sign(fiebre,coronavirus).
sign(fiebre,ebola).
sign(vomito,ebola).
sign(diarrea,ebola).
sign(erupciones_cutaneas,ebola).
sign(hemorragia,ebola).
sign(perdida_de_peso,ebola).
sign(lesiones_cutaneas,lepra).
sign(perdida_de_la_movilidad,lepra).
sign(paralisis,lepra).
sign(fiebre,malaria).
sign(vomito,malaria).
sign(fiebre,peste).
sign(vomito,peste).
sign(bubones,peste).
sign(llagas,peste).
sign(llagas,sifilis).
sign(erupciones_cutaneas,sifilis).
sign(fiebre,sifilis).
sign(inflamacion_de_los_ganglios_linfaticos,sifilis).
sign(perdida_de_pelo,sifilis).
sign(perdida_de_peso,sifilis).
sign(perdida_de_la_coordinacion,sifilis).
sign(paralisis,sifilis).
sign(sudoracion,tuberculosis).
sign(perdida_de_peso,tuberculosis).
sign(tos,tuberculosis).
sign(fiebre,difteria).
sign(lesiones_cutaneas,difteria).
sign(sangrado_nasal,difteria).
sign(tos,difteria).

test(test_PCR,coronavirus).
test(test_de_antigenos,coronavirus).
test(tomografia_de_torax,coronavirus).
test(test_ELISA,ebola).
test(test_PCR,ebola).
test(test_de_deteccion_de_anticuerpos,ebola).
test(test_de_seroneutralizacion,ebola).
test(cultivo_celular,ebola).
test(biopsia_de_piel,lepra).
test(lepromina_cutanea,lepra).
test(examen_fisico,malaria).
test(frotis_de_sangre,malaria).
test(test_con_tiras_reactivas,peste).
test(test_de_liquido_de_ulcera,sifilis).
test(ecocardiografia,sifilis).
test(angiografia_aortica,sifilis).
test(cateterismo_cardiaco,sifilis).
test(puncion_raquidea,sifilis).
test(examen_de_sangre,sifilis).
test(test_de_tuberculina,tuberculosis).
test(test_de_la_tuberculina,tuberculosis).
test(radiografia_de_torax,tuberculosis).
test(analisis_de_sangre,tuberculosis).
test(biopsia_de_higado,tuberculosis).
test(biopsia_de_ganglio_linfatico,tuberculosis).
test(tincion_de_Gram,difteria).
test(analisis_de_toxinas,difteria).
test(electrocardiograma,difteria).

treatment(remdesivir,coronavirus).
treatment(ritonavir,coronavirus).
treatment(lopinavir,coronavirus).
treatment(hidroxicloroquina,coronavirus).
treatment(dexametasona,coronavirus).
treatment(ivermectina,coronavirus).
treatment(soporte_respiratorio,coronavirus).
treatment(tomar_liquidos,ebola).
treatment(plasma_de_convaleciente,ebola).
treatment(suero_ZMapp,ebola).
treatment(preparado_de_globulina_hiperinmunizado,ebola).
treatment(molecula_AVI_7537,ebola).
treatment(antiviral_BCX4430,ebola).
treatment(favipiravir,ebola).
treatment(dapsona,lepra).
treatment(clofazimina,lepra).
treatment(rifampicina,lepra).
treatment(cloroquina,malaria).
treatment(artemisinina,malaria).
treatment(artemeter,malaria).
treatment(lumefantrina,malaria).
treatment(atovacuona_proguanil,malaria).
treatment(quinina,malaria).
treatment(doxiciclina,malaria).
treatment(clindamicina,malaria).
treatment(mefloquina,malaria).
treatment(artesunato,malaria).
treatment(estreptomicina,peste).
treatment(gentamicina,peste).
treatment(cloranfenicol,peste).
treatment(doxiciclina,peste).
treatment(ciprofloxacino,peste).
treatment(antibiotico,sifilis).
treatment(penicilina,sifilis).
treatment(isoniacida,tuberculosis).
treatment(rifampicina,tuberculosis).
treatment(etambutol,tuberculosis).
treatment(piracinamida,tuberculosis).
treatment(antitoxina_difterica,difteria).
treatment(penicilina,difteria).
treatment(eritromicina,difteria).

treatment(paracetamol,fiebre).
treatment(antibiotico,infeccion_bacteriana).
treatment(antivirales,inflamacion_pulmonar).

%Rules
sick(Patient, Disease) :- has(Patient, Symptom), symptom(Symptom, Disease).
sick(Patient, Disease) :- has(Patient, Sign), sign(Sign, Disease).
sick(Patient, Disease) :- has(Patient, Test), test(Test, Disease).

prescribe(Medicine, _, Disease) :- treatment(Medicine, Disease).
prescribe(Medicine, Patient, _) :- treatment(Medicine, X), has(Patient, X).
