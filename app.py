import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st
import matplotlib.pyplot as plt

# Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Train Brake Power Controller")
st.write("Descriptors : Distance (in m), Speed (in Kmph)")
st.write("Output Variable : Brake Power (in Percent)")
Distance_inp = st.slider("Distance", min_value=0, max_value=500)
Speed_inp = st.slider("Speed", min_value=0, max_value=60)
# Fuzzy Logic

Distance = ctrl.Antecedent(np.arange(0, 500, 1), 'Distance')
Speed = ctrl.Antecedent(np.arange(0, 60, 1), 'Speed')
BrakePower = ctrl.Consequent(np.arange(0, 100, 1), 'BrakePower')

Distance.automf(4, names=['Very Short Distance',
                          'Short Distance', 'Large Distance', 'Very Large Distance'])
Speed.automf(4, names=['Very Low Speed', 'Low Speed',
                       'High Speed', 'Very High Speed'])
BrakePower.automf(4, names=['Very Low Power',
                            'Low Power', 'High Power', 'Very High Power'])

st.write("Membership Function for Distance")
st.pyplot(Distance.view())
st.write("Membership Function for Speed")
st.pyplot(Speed.view())
st.write("Membership Function for Brake Power (in Percent)")
st.pyplot(BrakePower.view())


Rule_1 = ctrl.Rule(Distance['Very Short Distance'] &
                   Speed['Very Low Speed'], BrakePower['High Power'])
Rule_2 = ctrl.Rule(Distance['Very Short Distance']
                   & Speed['Low Speed'], BrakePower['High Power'])
Rule_3 = ctrl.Rule(Distance['Very Short Distance'] &
                   Speed['High Speed'], BrakePower['Very High Power'])
Rule_4 = ctrl.Rule(Distance['Very Short Distance'] &
                   Speed['Very High Speed'], BrakePower['Very High Power'])
Rule_5 = ctrl.Rule(Distance['Short Distance'] &
                   Speed['Very Low Speed'], BrakePower['Low Power'])
Rule_6 = ctrl.Rule(Distance['Short Distance'] &
                   Speed['Low Speed'], BrakePower['Low Power'])
Rule_7 = ctrl.Rule(Distance['Short Distance'] &
                   Speed['High Speed'], BrakePower['High Power'])
Rule_8 = ctrl.Rule(Distance['Short Distance'] &
                   Speed['Very High Speed'], BrakePower['High Power'])
Rule_9 = ctrl.Rule(Distance['Large Distance'] &
                   Speed['Very Low Speed'], BrakePower['Very Low Power'])
Rule_10 = ctrl.Rule(Distance['Large Distance'] &
                    Speed['Low Speed'], BrakePower['Very Low Power'])
Rule_11 = ctrl.Rule(Distance['Large Distance'] &
                    Speed['High Speed'], BrakePower['Low Power'])
Rule_12 = ctrl.Rule(Distance['Large Distance'] &
                    Speed['Very High Speed'], BrakePower['High Power'])
Rule_13 = ctrl.Rule(Distance['Very Large Distance'] &
                    Speed['Very Low Speed'], BrakePower['Very Low Power'])
Rule_14 = ctrl.Rule(Distance['Very Large Distance']
                    & Speed['Low Speed'], BrakePower['Very Low Power'])
Rule_15 = ctrl.Rule(Distance['Very Large Distance']
                    & Speed['High Speed'], BrakePower['Low Power'])
Rule_16 = ctrl.Rule(Distance['Very Large Distance']
                    & Speed['Very High Speed'], BrakePower['Low Power'])

st.write("Rules")
rule = st.selectbox('Select Rule:', [
                    "Rule_1", "Rule_2", "Rule_3", "Rule_4", "Rule_5", "Rule_6", "Rule_7", "Rule_8", "Rule_9", "Rule_10", "Rule_11", "Rule_12", "Rule_13", "Rule_14", "Rule_15", "Rule_16"])
if rule == "Rule_1":
    st.write(Rule_1)
    st.pyplot(ctrl.ControlSystem([Rule_1]).view())
elif rule == "Rule_2":
    st.write(Rule_2)
    st.pyplot(ctrl.ControlSystem([Rule_2]).view())
elif rule == "Rule_3":
    st.write(Rule_3)
    st.pyplot(ctrl.ControlSystem([Rule_3]).view())
elif rule == "Rule_4":
    st.write(Rule_4)
    st.pyplot(ctrl.ControlSystem([Rule_4]).view())
elif rule == "Rule_5":
    st.write(Rule_5)
    st.pyplot(ctrl.ControlSystem([Rule_5]).view())
elif rule == "Rule_6":
    st.write(Rule_6)
    st.pyplot(ctrl.ControlSystem([Rule_6]).view())
elif rule == "Rule_7":
    st.write(Rule_7)
    st.pyplot(ctrl.ControlSystem([Rule_7]).view())
elif rule == "Rule_8":
    st.write(Rule_8)
    st.pyplot(ctrl.ControlSystem([Rule_8]).view())
elif rule == "Rule_9":
    st.write(Rule_9)
    st.pyplot(ctrl.ControlSystem([Rule_9]).view())
elif rule == "Rule_10":
    st.write(Rule_10)
    st.pyplot(ctrl.ControlSystem([Rule_10]).view())
elif rule == "Rule_11":
    st.write(Rule_11)
    st.pyplot(ctrl.ControlSystem([Rule_11]).view())
elif rule == "Rule_12":
    st.write(Rule_12)
    st.pyplot(ctrl.ControlSystem([Rule_12]).view())
elif rule == "Rule_13":
    st.write(Rule_13)
    st.pyplot(ctrl.ControlSystem([Rule_13]).view())
elif rule == "Rule_14":
    st.write(Rule_14)
    st.pyplot(ctrl.ControlSystem([Rule_14]).view())
elif rule == "Rule_15":
    st.write(Rule_15)
    st.pyplot(ctrl.ControlSystem([Rule_15]).view())
elif rule == "Rule_16":
    st.write(Rule_16)
    st.pyplot(ctrl.ControlSystem([Rule_16]).view())


BrakingPower_ctrl = ctrl.ControlSystem(
    [Rule_1, Rule_2, Rule_3, Rule_4, Rule_5, Rule_6, Rule_7, Rule_8, Rule_9, Rule_10, Rule_11, Rule_12, Rule_13, Rule_14, Rule_15, Rule_16])
BrakingPower = ctrl.ControlSystemSimulation(BrakingPower_ctrl)


BrakingPower.input['Distance'] = Distance_inp
BrakingPower.input['Speed'] = Speed_inp

st.write("Calculate Brake Power")


BrakingPower.compute()
st.write(
    f"""### Brake Power (in Percent): {BrakingPower.output['BrakePower']} ###""")
st.pyplot(BrakePower.view(sim=BrakingPower))
