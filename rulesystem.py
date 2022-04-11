from experta import *

class RuleSystem(KnowledgeEngine):
    #Class init
    def __init__(self, sym_mapper, if_unmatched, fetch_treatments, fetch_diseaseDescription):
        self.sym_mapper = sym_mapper
        self.if_unmatched = if_unmatched
        self.fetch_diseaseDescription = fetch_diseaseDescription
        self.fetch_treatments = fetch_treatments
        KnowledgeEngine.__init__(self)

    #Starting point of the Expert System
    @DefFacts()
    def initiate_action(self):
        print(":::: Disease Prognosis System ::::\n")
        print("Provide symptoms: with severe, mild or no\n")
        yield Fact(action="identify_disease")

    #User inputs
    @Rule(Fact(action="identify_disease"), NOT(Fact(headache=W())), salience=5)
    def get_sym_1(self):
        self.declare(Fact(headache=input("headache: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(back_pain=W())), salience=1)
    def get_sym_2(self):
        self.declare(Fact(back_pain=input("back pain: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(chest_pain=W())), salience=1)
    def get_sym_3(self):
        self.declare(Fact(chest_pain=input("chest pain: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(cough=W())), salience=4)
    def get_sym_4(self):
        self.declare(Fact(cough=input("cough: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(fainting=W())), salience=1)
    def get_sym_5(self):
        self.declare(Fact(fainting=input("fainting: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(fatigue=W())), salience=1)
    def get_sym_6(self):
        self.declare(Fact(fatigue=input("fatigue: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(sunken_eyes=W())), salience=1)
    def get_sym_7(self):
        self.declare(Fact(sunken_eyes=input("sunken eyes: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(low_body_temp=W())), salience=1)
    def get_sym_8(self):
        self.declare(Fact(low_body_temp=input("low body temperature: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(restlessness=W())), salience=1)
    def get_sym_9(self):
        self.declare(Fact(restlessness=input("restlessness: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(sore_throat=W())), salience=1)
    def get_sym_10(self):
        self.declare(Fact(sore_throat=input("sore throat: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(fever=W())), salience=1)
    def get_sym_11(self):
        self.declare(Fact(fever=input("fever: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(nausea=W())), salience=1)
    def get_sym_12(self):
        self.declare(Fact(nausea=input("nausea: ")))

    @Rule(Fact(action="identify_disease"), NOT(Fact(blurred_vision=W())), salience=1)
    def get_sym_13(self):
        self.declare(Fact(blurred_vision=input("blurred_vision: ")))

    #Disease mapping
    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="mild"),
        Fact(back_pain="no"),
        Fact(chest_pain="mild"),
        Fact(cough="severe"),
        Fact(fainting="no"),
        Fact(sore_throat="mild"),
        Fact(fatigue="mild"),
        Fact(restlessness="mild"),
        Fact(low_body_temp="no"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Bronchitis"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="mild"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="mild"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="mild"),
        Fact(nausea="severe"),
        Fact(blurred_vision="no"),
    )
    def disease_1(self):
        self.declare(Fact(disease="Cholera"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="mild"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="severe"),
        Fact(fatigue="mild"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_2(self):
        self.declare(Fact(disease="Diphtheria"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="severe"),
        Fact(cough="mild"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="severe"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="mild"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="no"),
    )
    def disease_4(self):
        self.declare(Fact(disease="Giardiasis"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="mild"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="mild"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="no"),
    )
    def disease_5(self):
        self.declare(Fact(disease="Hepatitis"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="severe"),
        Fact(back_pain="no"),
        Fact(chest_pain="mild"),
        Fact(cough="no"),
        Fact(fainting="mild"),
        Fact(sore_throat="no"),
        Fact(fatigue="mild"),
        Fact(restlessness="mild"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="mild"),
    )
    def disease_6(self):
        self.declare(Fact(disease="Hypertension"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="severe"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="severe"),
        Fact(blurred_vision="no"),
    )
    def disease_7(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="severe"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="mild"),
    )
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="mild"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="mild"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="severe"),
        Fact(restlessness="mild"),
        Fact(low_body_temp="no"),
        Fact(fever="severe"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="no"),
    )
    def disease_9(self):
        self.declare(Fact(disease="Malaria"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="mild"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="mild"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="no"),
    )
    def disease_10(self):
        self.declare(Fact(disease="Pancreatitis"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="severe"),
        Fact(cough="severe"),
        Fact(fainting="no"),
        Fact(sore_throat="mild"),
        Fact(fatigue="mild"),
        Fact(restlessness="no"),
        Fact(low_body_temp="mild"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="no"),
    )
    def disease_11(self):
        self.declare(Fact(disease="Pneumonia"))

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="mild"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="severe"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="mild"),
    )
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))
    
    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="severe"),
        Fact(back_pain="no"),
        Fact(chest_pain="severe"),
        Fact(cough="severe"),
        Fact(fainting="no"),
        Fact(sore_throat="severe"),
        Fact(fatigue="severe"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="severe"),
        Fact(sunken_eyes="no"),
        Fact(nausea="mild"),
        Fact(blurred_vision="no"),
    )
    def disease_13(self):
        self.declare(Fact(disease="Coronavirus"))
        
    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="mild"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="mild"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="mild"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_14(self):
        self.declare(Fact(disease="Tetanus"))
        
        
    @Rule(
        Fact(action="identify_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="severe"),
        Fact(cough="mild"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="severe"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_15(self):
        self.declare(Fact(disease="Tuberculosis"))        


    #For disease unmatched to user input
    @Rule(Fact(action="identify_disease"), Fact(disease=MATCH.disease), salience=-938)
    def disease(self, disease):
        disease_name = disease
        disease_details = self.fetch_diseaseDescription(disease_name)
        treatments = self.fetch_treatments(disease_name)
        print("Disease Probability: %s\n" % (disease_name))
        print(disease_details)
        print("Treatment Suggestion:\n")
        print(treatments + "\n")

    @Rule(
        Fact(action="identify_disease"),
        Fact(headache=MATCH.headache),
        Fact(back_pain=MATCH.back_pain),
        Fact(chest_pain=MATCH.chest_pain),
        Fact(cough=MATCH.cough),
        Fact(fainting=MATCH.fainting),
        Fact(sore_throat=MATCH.sore_throat),
        Fact(fatigue=MATCH.fatigue),
        Fact(low_body_temp=MATCH.low_body_temp),
        Fact(restlessness=MATCH.restlessness),
        Fact(fever=MATCH.fever),
        Fact(sunken_eyes=MATCH.sunken_eyes),
        Fact(nausea=MATCH.nausea),
        Fact(blurred_vision=MATCH.blurred_vision),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999
    )
    def not_matched(
        self,
        headache,
        back_pain,
        chest_pain,
        cough,
        fainting,
        sore_throat,
        fatigue,
        restlessness,
        low_body_temp,
        fever,
        sunken_eyes,
        nausea,
        blurred_vision,
    ):
        print("\nNo exact disease mapped for the provided symptoms")
        symList = [
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            restlessness,
            low_body_temp,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision,
        ]
        exist_count = 0
        max_count = ""
        for key, val in self.sym_mapper.items():
            idx = 0
            temp = eval(key)
            for i in range(0, len(symList)):
                if temp[i] == symList[i] and (symList[i] == "severe" or symList[i] == "mild" or symList[i] == "yes"):
                    idx = idx + 1
            if idx > exist_count:
                exist_count = idx
                max_count = val
        if max_count != "":
            self.if_unmatched(max_count)