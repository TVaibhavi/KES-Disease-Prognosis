from rulesystem import RuleSystem
diseases_lst = []
diseases_sym_lst = []
sym_mapper = {}
diseases_descr_dict = {}
diseases_trt_dict = {}

#Read data from txt files
def preprocess():
    diseases = open("Data/diseases.txt")
    diseases_t = diseases.read()
    diseases_lst = diseases_t.split("\n")
    diseases.close()

    for disease in diseases_lst:
        disease_file = open("Data/Symptoms/" + disease + ".txt")
        disease_data = disease_file.read()
        s_lst = disease_data.split("\n")
        diseases_sym_lst.append(s_lst)
        sym_mapper[str(s_lst)] = disease
        disease_file.close()

        disease_file = open("Data/Details/" + disease + ".txt")
        disease_data = disease_file.read()
        diseases_descr_dict[disease] = disease_data
        disease_file.close()

        disease_file = open("Data/Treatments/" + disease + ".txt")
        disease_data = disease_file.read()
        diseases_trt_dict[disease] = disease_data
        disease_file.close()

#Find Disease
def identify_disease(*arguments):
    symptom_lst = []
    for symptom in arguments:
        symptom_lst.append(symptom)

    return sym_mapper[str(symptom_lst)]

#Retrieve disease details
def fetch_diseaseDescription(disease):
    return diseases_descr_dict[disease]

#Retrieve disease treatments
def fetch_treatments(disease):
    return diseases_trt_dict[disease]

#Handles unmatched symptoms
def if_unmatched(disease):
    disease_name = disease
    disease_details = fetch_diseaseDescription(disease_name)
    treatments = fetch_treatments(disease_name)
    print("\nDisease Probability: %s\n" % (disease_name))
    print(disease_details)
    print("Treatment Suggestion:\n")
    print(treatments + "\n")

#Driver function
if __name__ == "__main__":
    preprocess()
    engine = RuleSystem(sym_mapper, if_unmatched, fetch_treatments, fetch_diseaseDescription)
    while 1:
        engine.reset()
        engine.run()
        print("Would you like to continue?\nyes or no")
        if input() == "no":
            exit()
