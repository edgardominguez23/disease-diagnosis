%Facts, soruce: https://cuidateplus.marca.com/enfermedades/infecciosas.html
symptom(tos,coronavirus).
symptom(fatiga,coronavirus).
symptom(fiebre,coronavirus).
symptom(perdida_del_olfato,coronavirus).
symptom(perdida_del_gusto,coronavirus).
symptom(dolor_de_garganta,coronavirus).
symptom(dolor_de_cabeza,coronavirus).
symptom(disnea,coronavirus).
symptom(fiebre,ebola).
symptom(debilidad,ebola).
symptom(dolor_muscular,ebola).
symptom(dolor_de_cabeza,ebola).
symptom(dolor_de_garganta,ebola).
symptom(vomito,ebola).
symptom(diarrea,ebola).
symptom(erupciones_cutaneas,ebola).
symptom(disfuncion_renal,ebola).
symptom(disfuncion_hepatica,ebola).
symptom(hemorragia_interna,ebola).
symptom(hemorragia_externa,ebola).
symptom(anorexia,ebola).
symptom(cefalea,ebola).
symptom(mialgia,ebola).
symptom(artralgia,ebola).
symptom(dolor_de_torax,ebola).
symptom(nauseas,ebola).
symptom(dolor_abdominal,ebola).
symptom(dolor_epigastrico,ebola).
symptom(lesiones_cutaneas,lepra).
symptom(perdida_de_la_sensibilidad,lepra).
symptom(alteraciones_en_la_movilidad,lepra).
symptom(paralisis,lepra).
symptom(fiebre,malaria).
symptom(dolor_de_cabeza,malaria).
symptom(dolor_muscular,malaria).
symptom(escalofrios,malaria).
symptom(vomito,malaria).
symptom(fiebre,peste).
symptom(escalofrios,peste).
symptom(dolor_de_cabeza,peste).
symptom(debilidad,peste).
symptom(nauseas,peste).
symptom(vomito,peste).
symptom(bubones,peste).
symptom(llagas,peste).
symptom(llagas,sifilis).
symptom(erupciones_cutaneas,sifilis).
symptom(fiebre,sifilis).
symptom(inflamacion_de_los_ganglios_linfaticos,sifilis).
symptom(perdida_de_pelo,sifilis).
symptom(dolor_de_garganta,sifilis).
symptom(dolor_de_cabeza,sifilis).
symptom(perdida_de_peso,sifilis).
symptom(dolor_muscular,sifilis).
symptom(fatiga,sifilis).
symptom(perdida_de_la_coordinacion,sifilis).
symptom(paralisis,sifilis).
symptom(entumecimiento,sifilis).
symptom(demencia,sifilis).
symptom(ceguera,sifilis).
symptom(fatiga,tuberculosis).
symptom(malestar_general,tuberculosis).
symptom(sudoracion,tuberculosis).
symptom(perdida_de_peso,tuberculosis).
symptom(tos,tuberculosis).
symptom(dolor_de_garganta,difteria).
symptom(fiebre,difteria).
symptom(debilidad,difteria).
symptom(lesiones_cutaneas,difteria).
symptom(sangrado_nasal,difteria).
symptom(dificultad_para_respirar,difteria).
symptom(tos,difteria).

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
sick(Patient, Disease) :- has_symptom(Patient, Symptom), symptom(Symptom, Disease).
sick(Patient, Disease) :- has_test(Patient, Test), test(Test, Disease).

prescribe(Medicine, _, Disease) :- treatment(Medicine, Disease).
prescribe(Medicine, Patient, _) :- treatment(Medicine, Symptom), has_symptom(Patient, Symptom).
prescribe(Medicine, Patient, _) :- treatment(Medicine, Test), has_test(Patient, Test).