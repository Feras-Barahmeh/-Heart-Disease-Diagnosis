from RuleBase.Age import *
from RuleBase.BloodPressure import *
from RuleBase.Cholesterol import *
from RuleBase.BloodSugar import *
from RuleBase.LoweDensityLipoprotein import *
from RuleBase.HighDensityLipoprotein import *
from RuleBase.Risk import *

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
        ageRule.membershipDegrees(self.userAge)

        bloodRule = BloodPressure()
        bloodRule.trapezoidalMembership()
        bloodRule.draw()
        bloodRule.membershipDegrees(self.userBloodPressure)


        cholesterolRule = Cholesterol()
        cholesterolRule.trapezoidalMembership()
        cholesterolRule.draw()
        cholesterolRule.membershipDegrees(self.userCholesterol)

        bloodSugarRule = BloodSugar()
        bloodSugarRule.triangularMembership()
        bloodSugarRule.draw()
        bloodSugarRule.membershipDegrees(self.userBloodSugar)

        ldlRule = LoweDensityLipoprotein()
        ldlRule.triangularMembership()
        ldlRule.draw()
        ldlRule.membershipDegrees(self.userLDL)


        hdlRule = HighDensityLipoprotein()
        hdlRule.triangularMembership()
        hdlRule.draw()
        hdlRule.membershipDegrees(self.userHDL)

        riskRule = Risk()
        riskRule.trapezoidalMembership()
        riskRule.draw()