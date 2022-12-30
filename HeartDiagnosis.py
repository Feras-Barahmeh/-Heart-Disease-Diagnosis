from RuleBase.Age import *
from RuleBase.BloodPressure import *
from RuleBase.Cholesterol import *
from RuleBase.BloodSugar import *
from RuleBase.LoweDensityLipoprotein import *
from RuleBase.HighDensityLipoprotein import *
from RuleBase.Risk import *
from Rules import Rules
class HeartDiagnosis:
    def __init__(self):
        print("\t\tWelcome In Fuzzy Logic Hospital ❤❤")
        print("Enter health data for Heart Disease Risk Calculation with Fuzzy Logic")

        self.userAge            = getInformationUser("Enter Age: ")
        self.userBloodPressure  = getInformationUser("Enter Blood Pressure:  ")
        self.userCholesterol    = getInformationUser("Enter Cholesterol:  ")
        self.userBloodSugar     = getInformationUser("Enter BloodSugar:  ")
        self.userLDL            = getInformationUser("Enter Lowe Density Lipoprotein:  ")
        self.userHDL            = getInformationUser("Enter High Density Lipoprotein:  ")

        print("Thanks, Pleas Wait To Calculate Result 😊")

    def heartDiagnosis(self):
        ageRule = Age()
        ageRule.trapezoidalMembership()
        ageRule.draw()
        # Fuzzification
        ageRule.membershipDegrees(self.userAge)

        bloodRule = BloodPressure()
        bloodRule.trapezoidalMembership()
        bloodRule.draw()
        # Fuzzification
        bloodRule.membershipDegrees(self.userBloodPressure)

        cholesterolRule = Cholesterol()
        cholesterolRule.trapezoidalMembership()
        cholesterolRule.draw()
        # Fuzzification
        cholesterolRule.membershipDegrees(self.userCholesterol)

        bloodSugarRule = BloodSugar()
        bloodSugarRule.triangularMembership()
        bloodSugarRule.draw()
        # Fuzzification
        bloodSugarRule.membershipDegrees(self.userBloodSugar)

        ldlRule = LoweDensityLipoprotein()
        ldlRule.triangularMembership()
        ldlRule.draw()
        # Fuzzification
        ldlRule.membershipDegrees(self.userLDL)


        hdlRule = HighDensityLipoprotein()
        hdlRule.triangularMembership()
        hdlRule.draw()
        # Fuzzification
        hdlRule.membershipDegrees(self.userHDL)

        riskRule = Risk()
        riskRule.trapezoidalMembership()
        riskRule.draw()


        rules = Rules(ageRule=ageRule,
                      bloodRule=bloodRule,
                      cholesterolRule=cholesterolRule,
                      bloodSugarRule=bloodSugarRule,
                      ldlRule=ldlRule,
                      hdlRule=hdlRule,
                      riskRule=riskRule)

        # combining the fuzzified inputs according to the fuzzy rules to establish a rule strength
        rules.inferenceSystems()

        # cloudy inference engine using rules
        rules.cloudyInferenceEngine()

        risk0 = zeros_like(risk)

        fig, ax0 = plt.subplots(figsize=(7, 4))
        ax0.fill_between(risk, risk0, rules.uninfected, facecolor='r', alpha=0.7)
        ax0.plot(risk, rules.uninfected, 'r', linestyle='--')
        ax0.fill_between(risk, risk0, rules.little, facecolor='g', alpha=0.7)
        ax0.plot(risk, rules.little, 'g', linestyle='--')
        ax0.fill_between(risk, risk0, rules.mid, facecolor='b', alpha=0.7)
        ax0.plot(risk, rules.mid, 'b', linestyle='--')
        ax0.fill_between(risk, risk0, rules.high, facecolor='y', alpha=0.7)
        ax0.plot(risk, rules.high, 'y', linestyle='--')
        ax0.fill_between(risk, risk0, rules.veryHigh, facecolor='m', alpha=0.7)
        ax0.plot(risk, rules.veryHigh, 'm', linestyle='--')
        ax0.set_title('Out of the Risk')

        plt.tight_layout()

        # Defuzzification
        out_risk = fmax(fmax(fmax(fmax(rules.uninfected, rules.little), rules.mid), rules.high), rules.veryHigh)

        defuzzified = fuzz.defuzz(risk, out_risk, "mom") # mean of maximum

        result = fuzz.interp_membership(risk, out_risk, defuzzified)

        print("Coroner Heart Diagnosis:", defuzzified)


        fig, ax0 = plt.subplots(figsize=(7, 4))

        ax0.plot(risk, rules.uninfected, 'r', linewidth=0.5, linestyle='--')
        ax0.plot(risk, rules.little, 'g', linewidth=0.5, linestyle='--')
        ax0.plot(risk, rules.mid, 'b', linewidth=0.5, linestyle='--')
        ax0.plot(risk, rules.high, 'y', linewidth=0.5, linestyle='--')
        ax0.plot(risk, rules.veryHigh, 'm', linewidth=0.5, linestyle='--')

        ax0.fill_between(risk, risk0, out_risk, facecolor='Orange', alpha=0.7)
        ax0.plot([defuzzified, defuzzified], [0, result], 'k', linewidth=1.5, alpha=0.9)
        ax0.set_title('Mean of Maximum Defuzzification')

        plt.tight_layout()