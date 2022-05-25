import streamlit as st
from datetime import datetime
import time


now = datetime.now()

questions1 = [("In your social groups do you:", "Keep abreast of all happenings", "Be behind on the latest news"),
    ("With new company do you:", "Start conversations", "Wait to be approached"),
    ("Does new and non-routine interaction with others:", "Stimulate and energize you", "Tax your reserves"),
    ("Do you prefer:", "Many friends with brief contact", "A few friends with longer contact"),
    ("Do you:", "Speak easily and at length with strangers", "Find little to say to strangers"),
    ("Are you more inclined to be:", "Easy to approach", "Somewhat reserved")]



questions2 = [("Are you more:", "Realistic", "Speculative"),
    ("In doing ordinary things are you more likely to:", "Do it the usual way", "Do it your own way"),
    ("Facts:", "Speak for themselves", "Usually require interpretation"),
    ("Do you go more by:", "Facts", "Principles"),
    ("Are you more likely to trust your:", "Experience", "Hunch")]

#Not in the MBTI questions list
questions3 =  [("Is it worse to:", "Have your 'head in the clouds'", "Be 'in a rut'"),
    ("Are you more interested in:", "What is actual", "What is possible"),
    ("Are you more likely to:", "See how others are useful", "See how others see"),
    ("Do you feel:", "More practical than ingenious", "More ingenious than practical"),
    ("Is it harder for you to:", "Identify with others", "Use others")]


questions4 = [("Are you more impressed by:", "Principles", "Emotions"),
    ("Which appeals to you more:", "Consistency of thought", "Harmonious human relationships"),
    ("Are you inclined to be more:", "Cool headed", "Warm hearted"),
    ("Are you typically more a person of:", "Clear reason", "Strong feeling"),
    ("Which do you wish more for yourself:", "Clarity of reason", "Strength of compassion")]


questions5 =  [("Are you more drawn towards the:", "Convincing", "Touching"),
    ("Is it worse to be:", "Unjust", "Merciless"),
    ("Which rules you more:", "Your head", "Your heart"),
    ("Do you value in yourself more that you are:", "Unwavering", "Devoted"),
    ("Do you see yourself as basically:", "Hard-headed", "Soft-hearted")]


questions6 = [("Do you usually:", "Settle things", "Keep options open"),
    ("Should one usually let events occur:", "By careful selection and choice", "Randomly and by chance"),
    ("Which is more admirable:", "The ability to organize and be methodical", "The ability to adapt and make do"),
    ("Is it preferable mostly to:", "Make sure things are arranged", "Just let things happen"),
    ("Do you prefer the:", "Planned events", "Unplanned event")]


questions7 =  [("Do you tend to choose:", "Rather carefully", "Somewhat impulsively"),
    ("Does it bother you more having things:", "Incomplete", "Completed"),
    ("Would you say you are more:", "Serious and determined", "Easy-going"),
    ("Are you more comfortable:", "After a decision", "Before a decision"),
    ("Do you tend to be more:", "Deliberate than spontaneous", "Spontaneous than deliberate")]

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

with st.sidebar:
    class_code = st.text_input('Enter class code')
    #if class_code matches then the input and recommendation fields will appear

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
            #key_c += pc_code[1]
            #st.text(personality_code)
            st.text(key_c)
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
                            personality_code += pc_code[0]
                            key_c += pc_code[1]
                            #st.text(personality_code)
                            #st.text(key_c)
                            my_bar.progress(90)
                            pc_code = questions_print(questions7, key_c, 'J', 'P', pc_code[2], pc_code[3])
                            if pc_code != None:
                                personality_code += pc_code[0]
                                key_c += pc_code[1]
                                st.text(personality_code)
                                #st.text("Total number of questions answered"  + key_c)
                                my_bar.progress(100)
                                time.sleep(2)
                                placeholder6 =st.empty()
                                placeholder6.text("Congratulations! You have completed yoru MBTI test!")
                                st.balloons()
                                time.sleep(2)
                                placeholder6.empty()
                                test_complete = True
        if personality_code != "" and test_complete == True:
            st.header("Your MBTI is " + personality_code)
            #Test
            #url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
            #st.write("check out this [link](%s)" % url)

            if personality_code == "INFP":
                st.subheader(" The Mediator ")
                st.text("You can consider the following hobbie:")
                st.text("Poetry, creative writing, music, photography, theater, visual art")
                st.markdown('#')
                st.text("The following are some links you can check out")
                poetry_url = "https://tract.app/search?q=poetry"
                st.write("Check out this [Poetry](%s)" % poetry_url)
                cw_url = "https://tract.app/search?q=Creative%20writing"
                st.write("Check out this [Creative Writing](%s)" % cw_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music ](%s)" % mu_url)
                ph_url = "https://tract.app/search?q=photography"
                st.write("Check out this [Photography](%s)" % ph_url)
                th_url = "https://tract.app/search?q=theatre"
                st.write("Check out this [Theatre](%s)" % th_url)
                va_url = "https://tract.app/search?q=Visual%20Art"
                st.write("Check out this [Visual Art](%s)" % va_url)

            elif personality_code == "INFJ":
                st.subheader("The Advocate")
                st.text("You can consider the following hobbie:")
                st.text("Writing, art appreciation, reading, listening to music, cooking/baking, crafting")
                st.markdown('#')
                st.text("The following are some links you can check out")
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                ap_url = "https://tract.app/search?q=Art%20Appreciation"
                st.write("Check out this [Art Appreciation](%s)" % ap_url)
                rd_url = "https://tract.app/search?q=reading"
                st.write("Check out this [Reading](%s)" % rd_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music](%s)" % mu_url)
                ck_url = "https://tract.app/search?q=cooking"
                st.write("Check out this [Cooking](%s)" % ck_url)
                cr_url = "https://tract.app/search?q=crafting"
                st.write("Check out this [Crafting](%s)" % cr_url)

            elif personality_code == "ENFP":
                st.subheader("The Campaigner")
                st.text("You can consider the following hobbie:")
                st.text("Writing, creating art, playing instruments, listening to music, theater, reading fiction")
                st.markdown('#')
                st.text("The following are some links you can check out")
                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                ca_url = "https://tract.app/search?q=Creating%20Art"
                st.write("Check out this [Creating Art](%s)" % ca_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music](%s)" % mu_url)
                th_url = "https://tract.app/search?q=theatre"
                st.write("Check out this [Theatre](%s)" % th_url)
                fc_url = "https://tract.app/search?q=fiction"
                st.write("Check out this [Fiction](%s)" % fc_url)

            elif personality_code == "ENFJ":
                st.subheader("The Protagonist")
                st.text("You can consider the following hobbie:")
                st.text("Reading, storytelling, cooking, writing, music, organizing events") 

                wr_url = "https://tract.app/search?q=writing"
                st.write("Check out this [Writing](%s)" % wr_url)
                ck_url = "https://tract.app/search?q=cooking"
                st.write("Check out this [Cooking](%s)" % ck_url)
                st_url = "https://tract.app/search?q=storytelling"
                st.write("Check out this [Storytelling](%s)" % st_url)
                mu_url = "https://tract.app/search?q=music"
                st.write("Check out this [Music](%s)" % mu_url)




            elif personality_code == "INTJ":
                st.subheader("The Architect")
                st.text("You can consider the following hobbie:")
                st.text("Reading, computer and video games, independent sports (like swimming, skiing, not team based)")
            elif personality_code == "INTP":
                st.subheader("The Logician")
                st.text("You can consider the following hobbie:")
                st.text("Reading, chess, strategy games, writing, computer work (coding), hiking, backpacking, meditation")
            elif personality_code == "ENTJ":
                st.subheader("The Commander")
                st.text("You can consider the following hobbie:")
                st.text("Activities that would further their careers or where they can be in charge (sport team captain or learning how to computer code which they can use in their job)")
            elif personality_code == "ENTP":
                st.subheader("The Debator")
                st.text("You can consider the following hobbie:")
                st.text("Writing, art appreciation, sports, computer and video games, travel")
            elif personality_code == "ISFJ":
                st.subheader("The Defender")
                st.text("You can consider the following hobbie:")
                st.text("Cooking, gardening, painting, crafts, nature walks, watching movies")
            elif personality_code == "ISFP":
                st.subheader("The Adventurer")
                st.text("You can consider the following hobbie:")
                st.text("Activities that use physical/artistic skills - independent athletics, dance, craft projects (DIY); exploration is a big factor for them")
            elif personality_code == "ESFJ":
                st.subheader("The Consul")
                st.text("You can consider the following hobbie:")
                st.text("Cooking, volunteering, gardening, dancing, knitting, crafts")
            elif personality_code == "ESFP":
                st.subheader("The Entertainer")
                st.text("You can consider the following hobbie:")
                st.text("Team sports, home improvement projects, cooking, games, dance; they'll join any activity that sounds fun")
            elif personality_code == "ISTJ":
                st.subheader("The Logistician")
                st.text("You can consider the following hobbie:")
                st.text("Concentration games (trivia and chess), mind puzzles, computer games, physical fitness (gymming), solitary sports (golf)")
            elif personality_code == "ISTP":
                st.subheader("The Virtuso")
                st.text("You can consider the following hobbie:")
                st.text("Magic, comedy, archery, hunting, scuba diving, aviation, skydiving, extreme sports, risky activities with something mechanical involved")
            elif personality_code == "ESTJ":
                st.subheader("The Executive")
                st.text("You can consider the following hobbie:")
                st.text("Building, repairing, gardening, volunteering, playing sports - using their hands")
            elif personality_code == "ESTP":
                st.subheader("The Entrepreneur")
                st.text("You can consider the following hobbie:")
                st.text("Sports, or any athletics, risky activities (racing, boxing, flying)")

            st.markdown("#")    
            st.text("And to be clear - these are only suggestions. Do your own research into things you may like and just see where life takes you.")
            st.text("There are so many different types of hobbies in this world - don't limit yourself to just these.")
            st.markdown("#") 
            st.text("Just because one personality type says you'd be interested in certain hobbies doesn't give you the invitation to limit your personal exploration.")
            st.text(" Life is about learning things that interest you and while many feel their personality makes up their whole identity,")
            st.text("the truth is there is so much more to who you are. Your own preferences also help to shape that identity.")
            st.text("So go outside your comfort zone and try something new today! You may up surprising yourself.")


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