import streamlit as st
import streamlit as st
from fpdf import FPDF
import base64
from datetime import datetime
import time


now = datetime.now()

questions1 = [("Among your friends:", "I want to know the latest happenings", "I don't need to know the latest happenings"),
    ("Among strangers, do you:", "Start conversations", "Wait to be approached")]


questions2 = [("Are you more:", "Realistic", "Risk taking"),
    ("In doing ordinary things are you more likely to:", "Do it the usual way", "Do it your own way")]

#Not in the MBTI questions list
questions3 =  [("Is it worse to:", "Impractical and dreaming'", "Doing the same boring things"),
    ("Are you more interested in:", "What is actual", "What is possible")]


questions4 = [("Are you more impressed by:", "Principles", "Emotions"),
    ("Which appeals to you more:", "Consistency of thought", "Harmonious human relationships")]


questions5 =  [("Are you more drawn towards the:", "Convincing", "Touching"),
    ("Is it worse to be:", "Unjust", "Merciless")]


questions6 = [("Do you usually:", "Settle things", "Keep options open"),
    ("Should one usually let events occur:", "By careful selection and choice", "Randomly and by chance")]


questions7 =  [("Do you tend to choose:", "Rather carefully", "Somewhat impulsively"),
    ("Does it bother you more having things:", "Incomplete", "Completed")]

def questions_print(question_list, key_counter, pc_a, pc_b, ca, cb):
    ans_counter = 0
    answer = ""
    counter_a, counter_b = ca, cb
    pc = ""
    for question in question_list:
        
        #st.text(key_counter)
        placeholder1 =st.empty()
        placeholder2 =st.empty()
        placeholder3 =st.empty()
        placeholder4 =st.empty()
        placeholder5 =st.empty()
        placeholder1.text(question[0])
        placeholder2.text("(A) " + question[1])
        placeholder3.text("(B) " + question[2])
        placeholder5.markdown('#')
        answer = placeholder4.selectbox('Choose one', ['Select','A', 'B'], key = key_counter)
        if answer == "A":
            counter_a += 1
            ans_counter += 1
        elif answer == "B":
            counter_b += 1
            ans_counter += 1    
        key_counter += 1    
        if answer != 'Select':
            placeholder1.empty()
            placeholder1.empty()
            placeholder2.empty()
            placeholder3.empty()
            placeholder4.empty()
            placeholder5.empty()

    if counter_a > counter_b:
        #st.text('Your first personality code is: E')
        pc = pc_a
    else:
        #st.text('Your first personality code is: I')
        pc = pc_b

    if len(question_list) == ans_counter:
        return pc,key_counter, counter_a, counter_b


st.title("Interests 🤔 & Personality 😃 Profiling")

# with st.sidebar:
#     class_code = st.text_input('Enter class code')
#     #if class_code matches then the input and recommendation fields will appear

def main():
    
    personality_code  = ""
    pc_code = ""
    key_c = 0
    test_complete = False
    #key_counter = 0
    #if class code is valid, the rest of the input functions will appear
    #st.header("Please key in the necessary details")
    #st.text("Please note that this test is a simple adaptation of the Myers Briggs test, the results helps direct you to suggested area of interests based on your personality")
    #st.text("The result of this test is a not an accurate protrayal of your personality based on the actual Myers Briggs test, you should take the actual Myers Briggs test conducted by a qualified tester")
    # stu_name = st.text_input("Hi there, please tell me your name!")

    #question 1
    st.caption("Please choose A or B that best describes you")
    st.caption("The questions will disappear after you have answered them")
    st.markdown('#')

    my_bar = st.progress(0)
    pc_code = questions_print(questions1, key_c, 'E', 'I', 0, 0)
    if pc_code != None:
        personality_code += pc_code[0]
        key_c += pc_code[1]
        #st.text(personality_code)
        #st.text(key_c)
        my_bar.progress(15)
        pc_code = questions_print(questions2, key_c, 'S', 'N', 0, 0)
        if pc_code != None:
            #personality_code += pc_code[0]
            key_c += pc_code[1]
            #st.text(personality_code)
            #st.text(key_c)
            my_bar.progress(30)
            pc_code = questions_print(questions3, key_c, 'S', 'N', pc_code[2], pc_code[3])
            if pc_code != None:
                personality_code += pc_code[0]
                key_c += pc_code[1]
                #st.text(personality_code)
                #st.text(key_c)
                my_bar.progress(45)
                pc_code = questions_print(questions4, key_c, 'T', 'F', 0, 0)
                if pc_code != None:
                    #personality_code += pc_code[0]
                    key_c += pc_code[1]
                    #st.text(personality_code)
                    #st.text(key_c)
                    my_bar.progress(60)
                    pc_code = questions_print(questions5, key_c, 'T', 'F', pc_code[2], pc_code[3])
                    if pc_code != None:
                        personality_code += pc_code[0]
                        key_c += pc_code[1]
                        #st.text(personality_code)
                        my_bar.progress(75)
                        #st.text(key_c)
                        pc_code = questions_print(questions6, key_c, 'J', 'P', 0, 0)
                        if pc_code != None:
                            #personality_code += pc_code[0]
                            key_c += pc_code[1]
                            #st.text(personality_code)
                            #st.text(key_c)
                            my_bar.progress(90)
                            pc_code = questions_print(questions7, key_c, 'J', 'P', pc_code[2], pc_code[3])
                            if pc_code != None:
                                personality_code += pc_code[0]
                                key_c += pc_code[1]
                                #st.subheader(personality_code)
                                #st.text("Total number of questions answered"  + key_c)
                                my_bar.progress(100)
                                #time.sleep(2)
                                placeholder6 =st.empty()
                                placeholder6.text("Congratulations! You have completed your personality test!")
                                st.balloons()
                                time.sleep(2)
                                placeholder6.empty()
                                test_complete = True
        if personality_code != "" and test_complete == True:
            st.header("Results of the Personality and Interests test")
            list_url = []
            #Test
            #url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
            #st.write("check out this [link](%s)" % url)

            if personality_code == "INFP":
                #st.subheader(" The Mediator ")
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Poetry, creative writing, music, photography, theater, visual art")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                poetry_url = "https://tract.app/search?q=poetry"
                st.write("Check out this [Poetry](%s)" % poetry_url)
                list_url.append("Poerty")
                list_url.append(poetry_url)
                cw_url = "https://tract.app/search?q=Creative%20writing"
                st.write("Check out this [Creative Writing](%s)" % cw_url)
                list_url.append("Writing")
                list_url.append(cw_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music ](%s)" % mu_url)
                list_url.append("Music")
                list_url.append(mu_url)
                ph_url = "https://tract.app/search?q=photography"
                st.write("Check out this [Photography](%s)" % ph_url)
                list_url.append("Photography")
                list_url.append(ph_url)
                th_url = "https://tract.app/search?q=theatre"
                st.write("Check out this [Theatre](%s)" % th_url)
                list_url.append("Theatre")
                list_url.append(th_url)
                va_url = "https://tract.app/search?q=Visual%20Art"
                st.write("Check out this [Visual Art](%s)" % va_url)
                list_url.append("Visual Arts")
                list_url.append(va_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Mediator")
                mbti_url = "https://www.16personalities.com/infp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")
                #PDF report
                profile_text = """Your MBTI Profile is INFF, also known as The Mediator"""
                hobbies_text = """You can consider the following hobbies: Poetry, creative writing, music, photography, theater, visual art"""

            elif personality_code == "INFJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Writing, art appreciation, reading, listening to music, cooking/baking, crafting")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                list_url.append("Writing")
                list_url.append(wr_url)
                ap_url = "https://tract.app/search?q=Art%20Appreciation"
                st.write("Check out this [Art Appreciation](%s)" % ap_url)
                list_url.append("Art Appreciation")
                list_url.append(ap_url)
                rd_url = "https://tract.app/search?q=reading"
                st.write("Check out this [Reading](%s)" % rd_url)
                list_url.append("Reading")
                list_url.append(rd_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music](%s)" % mu_url)
                list_url.append("Music")
                list_url.append(mu_url)
                ck_url = "https://tract.app/search?q=recipe"
                st.write("Check out this [Cooking](%s)" % ck_url)
                list_url.append("Cooking")
                list_url.append(ck_url)
                cr_url = "https://tract.app/search?q=crafting"
                st.write("Check out this [Crafting](%s)" % cr_url)
                list_url.append("Crafting")
                list_url.append(cr_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Advocate")
                mbti_url = "https://www.16personalities.com/infj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is INFJ, also known as The Advocate"""
                hobbies_text = """You can consider the following hobbies: Writing, art appreciation, reading, listening to music, cooking/baking, craftings"""


            elif personality_code == "ENFP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Writing, creating art, playing instruments, music, theater, reading fiction")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                list_url.append("Writing")
                list_url.append(wr_url)
                ca_url = "https://tract.app/search?q=Creating%20Art"
                st.write("Check out this [Creating Art](%s)" % ca_url)
                list_url.append("Creating Arts")
                list_url.append(ca_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music](%s)" % mu_url)
                list_url.append("Music")
                list_url.append(mu_url)
                th_url = "https://tract.app/search?q=theatre"
                st.write("Check out this [Theatre](%s)" % th_url)
                list_url.append("Theatre")
                list_url.append(th_url)
                fc_url = "https://tract.app/search?q=fiction"
                st.write("Check out this [Fiction](%s)" % fc_url)
                list_url.append("Fiction")
                list_url.append(fc_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Campaigner")
                mbti_url = "https://www.16personalities.com/enfp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report #
                profile_text = """Your MBTI Profile is ENFP, also known as The Campaigner"""
                hobbies_text = """You can consider the following hobbies: Writing, creating art, playing instruments, music, theater, reading fiction"""

            elif personality_code == "ENFJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Reading, storytelling, cooking, writing, music, organizing events")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                list_url.append("Writing")
                list_url.append(wr_url)
                ck_url = "https://tract.app/search?q=recipe"
                st.write("Check out this [Cooking](%s)" % ck_url)
                list_url.append("Cooking")
                list_url.append(ck_url)
                st_url = "https://tract.app/search?q=storytelling"
                st.write("Check out this [Storytelling](%s)" % st_url)
                list_url.append("Storytelling")
                list_url.append(st_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music](%s)" % mu_url)
                list_url.append("Music")
                list_url.append(mu_url)
                rd_url = "https://tract.app/search?q=reading"
                st.write("Check out this [Reading](%s)" % rd_url)
                list_url.append("Reading")
                list_url.append(rd_url)
                oe_url = "https://tract.app/search?q=leader"
                st.write("Check out this [Leadership](%s)" % oe_url)
                list_url.append("Reading")
                list_url.append(oe_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Protagonist")
                mbti_url = "https://www.16personalities.com/enfj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ENFJ, also known as The Protagonist"""
                hobbies_text = """You can consider the following hobbies: Reading, storytelling, cooking, writing, music, organizing events"""

            elif personality_code == "INTJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Reading, computer and video games, independent sports (like swimming, skiing)")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                rd_url = "https://tract.app/search?q=reading"
                st.write("Check out this [Reading](%s)" % rd_url)
                list_url.append("Reading")
                list_url.append(rd_url)
                vg_url = "https://tract.app/search?q=computer%20games"
                st.write("Check out this [Computer Games](%s)" % vg_url)
                list_url.append("Computer Games")
                list_url.append(vg_url)
                sp_url = "https://tract.app/search?q=sports"
                st.write("Check out this [Sports](%s)" % sp_url)
                list_url.append("Sports")
                list_url.append(sp_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Architect")
                mbti_url = "https://www.16personalities.com/intj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is INTJ, also known as The Architect"""
                hobbies_text = """You can consider the following hobbies: Reading, computer and strategy games, independent sports (like swimming, skiing)"""

            elif personality_code == "INTP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Reading, chess, strategy games, writing, computer work (coding), hiking, backpacking, meditation")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                rd_url = "https://tract.app/search?q=reading"
                st.write("Check out this [Reading](%s)" % rd_url)
                list_url.append("Reading")
                list_url.append(rd_url)
                ch_url = "https://tract.app/search?q=chess"
                st.write("Check out this [Chess(%s)" % ch_url)
                list_url.append("Chess")
                list_url.append(ch_url)
                sg_url = "https://tract.app/search?q=strategy%20games"
                st.write("Check out this [Strategy Games](%s)" % sg_url)
                list_url.append("Strategy Games")
                list_url.append(sg_url)
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                list_url.append("Writing")
                list_url.append(wr_url)
                cd_url = "https://tract.app/search?q=coding"
                st.write("Check out this [Coding](%s)" % cd_url)
                list_url.append("Coding")
                list_url.append(cd_url)
                hk_url = "https://tract.app/search?q=hiking"
                st.write("Check out this [Hiking](%s)" % hk_url)
                list_url.append("Hiking")
                list_url.append(hk_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Logician")
                mbti_url = "https://www.16personalities.com/intp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")
                
                #PDF report
                profile_text = """Your MBTI Profile is INTP, also known as The Logician"""
                hobbies_text = """You can consider the following hobbies: Reading, chess, strategy games, writing, computer work (coding), hiking"""

            elif personality_code == "ENTJ":
                st.markdown('#')
                st.subheader("Based on the survey, you can consider the following hobbies:")
                st.subheader("Activities that would further their careers or where they can be in charge")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                cd_url = "https://tract.app/search?q=coding"
                st.write("Check out this [Coding](%s)" % cd_url)
                list_url.append("Coding")
                list_url.append(cd_url)
                sg_url = "https://tract.app/search?q=strategy%20games"
                st.write("Check out this [Video Games](%s)" % sg_url)
                list_url.append("Strategy Games")
                list_url.append(sg_url)
                ld_url = "https://tract.app/search?q=leadership"
                st.write("Check out this [Leadership](%s)" % ld_url)
                list_url.append("Leadership")
                list_url.append(ld_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Commander")
                mbti_url = "https://www.16personalities.com/entj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ENTJ, also known as The Commander"""
                hobbies_text = """You can consider the following hobbies: Activities that would further their careers or where they can be in charge"""

            elif personality_code == "ENTP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Writing, art appreciation, sports, computer and video games, travel")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                list_url.append("Writing")
                list_url.append(wr_url)
                ap_url = "https://tract.app/search?q=Art%20Appreciation"
                st.write("Check out this [Art Appreciation](%s)" % ap_url)
                list_url.append("Art Appreciation")
                list_url.append(ap_url)
                sp_url = "https://tract.app/search?q=sports"
                st.write("Check out this [Sports](%s)" % sp_url)
                list_url.append("Sports")
                list_url.append(sp_url)
                vg_url = "https://tract.app/search?q=computer%20games"
                st.write("Check out this [Computer Games](%s)" % vg_url)
                list_url.append("Computer Games")
                list_url.append(vg_url)
                tr_url = "https://tract.app/search?q=travel"
                st.write("Check out this [Travel](%s)" % tr_url)
                list_url.append("Travel")
                list_url.append(tr_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Debator")
                mbti_url = "https://www.16personalities.com/entp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ENTP, also known as The Debator"""
                hobbies_text = """You can consider the following hobbies: Writing, art appreciation, sports, computer and video games, travel"""

            elif personality_code == "ISFJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Cooking, gardening, painting, crafts, nature walks, watching movies")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                ck_url = "https://tract.app/search?q=recipe"
                st.write("Check out this [Cooking](%s)" % ck_url)
                list_url.append("Cooking")
                list_url.append(ck_url)
                gd_url = "https://tract.app/search?q=gardening"
                st.write("Check out this [Gardening](%s)" % gd_url)
                list_url.append("Gardening")
                list_url.append(gd_url)
                cr_url = "https://tract.app/search?q=crafts"
                st.write("Check out this [Crafts](%s)" % cr_url)
                list_url.append("Crafts")
                list_url.append(cr_url)
                na_url = "https://tract.app/search?q=nature"
                st.write("Check out this [Nature](%s)" % na_url)
                list_url.append("Nature")
                list_url.append(na_url)
                mv_url = "https://tract.app/search?q=movies"
                st.write("Check out this [Movies](%s)" % mv_url)
                list_url.append("Movies")
                list_url.append(mv_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Defender")
                mbti_url = "https://www.16personalities.com/isfj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ISFJ, also known as The Defender"""
                hobbies_text = """You can consider the following hobbies: Cooking, gardening, painting, crafts, nature walks, watching movies"""

            elif personality_code == "ISFP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Athletics, dance, craft projects (DIY)")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                cr_url = "https://tract.app/search?q=crafts"
                st.write("Check out this [Crafts](%s)" % cr_url)
                list_url.append("Crafts")
                list_url.append(cr_url)
                at_url = "https://tract.app/search?q=athletics"
                st.write("Check out this [Athletics](%s)" % at_url)
                list_url.append("Athletics")
                list_url.append(at_url)
                da_url = "https://tract.app/search?q=dance"
                st.write("Check out this [Dance](%s)" % da_url)
                list_url.append("Dance")
                list_url.append(da_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Adventurer")
                mbti_url = "https://www.16personalities.com/isfp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ISFP, also known as The Adventurer"""
                hobbies_text = """You can consider the following hobbies: Athletics, dance, craft projects (DIY)"""


            elif personality_code == "ESFJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Cooking, volunteering, gardening, dancing, knitting, crafts")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                ck_url = "https://tract.app/search?q=recipe"
                st.write("Check out this [Cooking](%s)" % ck_url)
                list_url.append("Cooking")
                list_url.append(ck_url)
                gd_url = "https://tract.app/search?q=gardening"
                st.write("Check out this [Gardening](%s)" % gd_url)
                list_url.append("Gardening")
                list_url.append(gd_url)
                cr_url = "https://tract.app/search?q=crafts"
                st.write("Check out this [Crafts](%s)" % cr_url)
                list_url.append("Crafts")
                list_url.append(cr_url)
                da_url = "https://tract.app/search?q=dance"
                st.write("Check out this [Dance](%s)" % da_url)
                list_url.append("Dance")
                list_url.append(da_url)
                kn_url = "https://tract.app/search?q=knitting"
                st.write("Check out this [Knitting](%s)" % kn_url)
                list_url.append("Knitting")
                list_url.append(kn_url)
                vn_url = "https://tract.app/search?q=charity"
                st.write("Check out this [Volunteering](%s)" % vn_url)
                list_url.append("Volunteering")
                list_url.append(vn_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Consul")
                mbti_url = "https://www.16personalities.com/esfj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ESFJ, also known as The Consul"""
                hobbies_text = """You can consider the following hobbies: Cooking, athletics, dance, craft projects (DIY)"""


            elif personality_code == "ESFP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Team sports, home improvement projects, cooking, games, dance")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                ck_url = "https://tract.app/search?q=recipe"
                st.write("Check out this [Cooking](%s)" % ck_url)
                list_url.append("Cooking")
                list_url.append(ck_url)
                da_url = "https://tract.app/search?q=dance"
                st.write("Check out this [Dance](%s)" % da_url)
                list_url.append("Dance")
                list_url.append(da_url)
                sp_url = "https://tract.app/search?q=sports"
                st.write("Check out this [Sports](%s)" % sp_url)
                list_url.append("Sports")
                list_url.append(sp_url)
                hi_url = "https://tract.app/search?q=home%20improvement"
                st.write("Check out this [Home improvement](%s)" % hi_url)
                list_url.append("Home Improvement")
                list_url.append(hi_url)
                ga_url = "https://tract.app/search?q=games"
                st.write("Check out this [Games](%s)" % ga_url)
                list_url.append("Games")
                list_url.append(ga_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Entertainer")
                mbti_url = "https://www.16personalities.com/esfp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ESFP, also known as The Entertainer"""
                hobbies_text = """You can consider the following hobbies: Team sports, home improvement projects, cooking, games, dance"""


            elif personality_code == "ISTJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Chess, mind puzzles, computer games, physical fitness, solitary sports (golf)")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                pz_url = "https://tract.app/search?q=puzzles"
                st.write("Check out this [Puzzles](%s)" % pz_url)
                list_url.append("Puzzles")
                list_url.append(pz_url)
                ch_url = "https://tract.app/search?q=chess"
                st.write("Check out this [Chess](%s)" % ch_url)
                list_url.append("Chess")
                list_url.append(ch_url)
                vg_url = "https://tract.app/search?q=computer%20games"
                st.write("Check out this [Computer Games](%s)" % vg_url)
                list_url.append("Computer Games")
                list_url.append(vg_url)
                ft_url = "https://tract.app/search?q=fitness"
                st.write("Check out this [Fitness](%s)" % ft_url)
                list_url.append("Fitness")
                list_url.append(ft_url)
                gf_url = "https://tract.app/search?q=golf"
                st.write("Check out this [Golf](%s)" % gf_url)
                list_url.append("Golf")
                list_url.append(gf_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Logistician")
                mbti_url = "https://www.16personalities.com/istj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ISTJ, also known as The Logistician"""
                hobbies_text = """You can consider the following hobbies: Chess, mind puzzles, computer games, physical fitness, solitary sports (golf)"""


            elif personality_code == "ISTP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Magic, comedy, archery, scuba diving, aviation, skydiving and sports ")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                mg_url = "https://tract.app/search?q=magic"
                st.write("Check out this [Magic](%s)" % mg_url)
                list_url.append("Magic")
                list_url.append(mg_url)
                cy_url = "https://tract.app/search?q=comedy"
                st.write("Check out this [Comedy](%s)" % cy_url)
                list_url.append("Comedy")
                list_url.append(cy_url)
                ay_url = "https://tract.app/search?q=archery"
                st.write("Check out this [Archery](%s)" % ay_url)
                list_url.append("Archery")
                list_url.append(ay_url)
                av_url = "https://tract.app/search?q=aviation"
                st.write("Check out this [Aviation](%s)" % av_url)
                list_url.append("Aviation")
                list_url.append(av_url)
                sk_url = "https://tract.app/search?q=skydiving"
                st.write("Check out this [Skydiving](%s)" % sk_url)
                list_url.append("Skydiving")
                list_url.append(sk_url)
                sp_url = "https://tract.app/search?q=sports"
                st.write("Check out this [Sports](%s)" % sp_url)
                list_url.append("Sports")
                list_url.append(sp_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Virtuso")
                mbti_url = "https://www.16personalities.com/istp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ISTP, also known as The Virtuso"""
                hobbies_text = """You can consider the following hobbies: Magic, comedy, archery, scuba diving, aviation, skydiving and sports"""

            elif personality_code == "ESTJ":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Building, repairing, gardening, volunteering, playing sports")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                bd_url = "https://tract.app/search?q=building"
                st.write("Check out this [Building](%s)" % bd_url)
                list_url.append("Building")
                list_url.append(bd_url)
                rp_url = "https://tract.app/search?q=repairing"
                st.write("Check out this [Repairing](%s)" % rp_url)
                list_url.append("Repairing")
                list_url.append(rp_url)
                gd_url = "https://tract.app/search?q=gardening"
                st.write("Check out this [Gardening](%s)" % gd_url)
                list_url.append("Gardening")
                list_url.append(gd_url)
                vn_url = "https://tract.app/search?q=charity"
                st.write("Check out this [Volunteering](%s)" % vn_url)
                list_url.append("Volunteering")
                list_url.append(vn_url)
                sp_url = "https://tract.app/search?q=sports"
                st.write("Check out this [Sports](%s)" % sp_url)
                list_url.append("Sports")
                list_url.append(sp_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Executive")
                mbti_url = "https://www.16personalities.com/estj-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")

                #PDF report
                profile_text = """Your MBTI Profile is ESTJ, also known as The Executive"""
                hobbies_text = """You can consider the following hobbies: Building, repairing, gardening, volunteering, playing sports"""

            elif personality_code == "ESTP":
                st.markdown('#')
                st.write("Based on the survey, you can consider the following hobbies:")
                st.subheader("Sports, any athletics, racing or flying")
                st.markdown('#')
                st.write("The following are some links you can check out")
                st.write("Please login to Tract.app before clicking the links")
                sp_url = "https://tract.app/search?q=sports"
                st.write("Check out this [Sports](%s)" % sp_url)
                list_url.append("Sports")
                list_url.append(sp_url)
                at_url = "https://tract.app/search?q=athletics"
                st.write("Check out this [Athletics](%s)" % at_url)
                list_url.append("Athletics")
                list_url.append(at_url)
                rc_url = "https://tract.app/search?q=racing"
                st.write("Check out this [Racing](%s)" % rc_url)
                list_url.append("Racing")
                list_url.append(rc_url)
                fl_url = "https://tract.app/search?q=flying"
                st.write("Check out this [Flying](%s)" % fl_url)
                list_url.append("Flying")
                list_url.append(fl_url)
                st.markdown('#')
                st.write("Your MBTI profile is assesed as " + personality_code + ", also known as The Entrepreneur")
                mbti_url = "https://www.16personalities.com/estp-personality"
                st.write("If you are interested to know more about MBTI profile, you can access this [link](%s)" % mbti_url)
                st.write("Do note that the test is not comprehensive and you should consider taking a more thorough test to find get a more accurate MBTI assessment")
                #PDF report
                profile_text = "Your MBTI Profile is ESTP, also known as The Entrepreneur"
                hobbies_text = "You can consider the following hobbies: Sports, any athletics, racing or flying"

            st.markdown("#")
            st.write("These hobbies are just suggestions.")    
            st.write("Should Tract.app does not match or return any suitable interest resources,")
            st.write("please explore other websites or video sharing sites to help pursue your interests")
            st.markdown("#") 
            title_text = "MBTI and Interest Profile Report"
            link_intro_text = "The following are some links you can check out: (Login to Tract.app before clicking the links)"

            export_as_pdf = st.button("Export Report")     

            def create_download_link(val, filename):
                b64 = base64.b64encode(val)  # val looks like b'...'
                return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

            if export_as_pdf:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial', 'B', 16)
                pdf.cell(40, 10, title_text, ln = 1)
                pdf.set_text_color(255,0,0)
                pdf.set_font('Arial', 'U', 12)
                pdf.cell(40, 10, profile_text, ln = 2)
                pdf.set_text_color(0,0,0)
                pdf.set_font('Arial', '', 12)
                pdf.cell(40, 10, hobbies_text, ln = 3)
                pdf.set_font('Arial', '', 12)
                pdf.cell(40, 10, link_intro_text, ln = 4)
                pdf.set_text_color(0,0,255)
                pdf.set_font('Arial', 'U', 12)

                i = 0
                while i < len(list_url):
                    pdf.cell(40,10,txt = list_url[i], ln = 5 + i, link = list_url[i + 1])
                    i += 2 
        
                html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Personality and Hobbies Report")

                st.markdown(html, unsafe_allow_html=True)
            # st.write("Just because one personality type says you'd be interested in certain hobbies ")
            # st.write("doesn't give you the invitation to limit your personal exploration.")
            # st.write("Life is about learning things that interest you and ")
            # st.write("while many feel their personality makes up their whole identity,")
            # st.write("the truth is there is so much more to who you are. ")
            # st.write("Your own preferences also help to shape that identity.")
            # st.write("So go outside your comfort zone and try something new today! ")
            # st.write("You may up surprising yourself.")


if __name__ == "__main__":
    main()



    # for question in questions1:
    #     answer = ""
    #     #st.text(key_counter)
    #     placeholder1 =st.empty()
    #     placeholder2 =st.empty()
    #     placeholder3 =st.empty()
    #     placeholder4 =st.empty()
    #     placeholder5 =st.empty()
    #     placeholder1.text(question[0])
    #     placeholder2.text("(A) " + question[1])
    #     placeholder3.text("(B) " + question[2])
    #     placeholder5.markdown('#')
    #     answer = placeholder4.selectbox('Choose one', ['Select','A', 'B'], key = key_counter)
    #     if answer == "A":
    #         counter_a += 1
    #     else:
    #         counter_b += 1
        
    #     key_counter += 1    
    #     if answer != 'Select':
    #         placeholder1.empty()
    #         placeholder1.empty()
    #         placeholder2.empty()
    #         placeholder3.empty()
    #         placeholder4.empty()
    #         placeholder5.empty()

    # if counter_a > counter_b:
    #     st.text('Your first personality code is: E')
    #     personality_code = personality_code + "E"
    # else:
    #     st.text('Your first personality code is: I')
    #     personality_code = personality_code + "I"