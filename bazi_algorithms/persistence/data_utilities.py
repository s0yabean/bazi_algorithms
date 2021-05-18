
from flask import session

def sessions_reset():
    pass
    # session["mbti_obj"] = MbtiClassBuilder(2, 5)
    # session["probs_hundred"] = [25, 25, 25, 25]
    # session["input_text"] = []
    # session["progress_percentage"] = 0
    # session["profile_name"] = "test name"

# def sessions_ai_form_submit(result, text):
#     session["mbti_obj"] = session["mbti_obj"].mass_add(result, mult=1)
#     session["probs_hundred"] = mc_estimate(
# session["mbti_obj"].show_dict(), 10000, probRep.HUNDRED
#     )
#     session["input_text"] = append_input(session["input_text"], text)
#     session["progress_percentage"] = min(100, session["progress_percentage"] + 20)

# def sessions_chart_data():
#     if session["progress_percentage"] == 0:
#         progress_message = "Start Adding Data (Recommended 5 Posts)."
#     elif session["progress_percentage"] == 100:
#         progress_message = (
#             "Enough Data (Add More For Better Results). Total Posts: "
#             + str(len(session["input_text"]))
#         )
#     elif session["progress_percentage"] == 80:
#         progress_message = "4 Posts Submitted. 1 More Recommended."
#     else:
#         progress_message = (
#             "Post Submitted. "
#             + str(int(5 - session["progress_percentage"] / 20))
#             + " More Recommended."
#         )
#     return progress_message

# def append_input(input_list, text):
#     input_list.append(text)
#     return input_list
