import streamlit as st
from datetime import datetime
import time


now = datetime.now()

questions1 = [("At a party do you:", "interact with many, including strangers", "interact with a few, known  to you"),
    ("At parties do you:", "Stay late, with increasing energy", "Leave early, with decreasing energy"),
    ("In your social groups do you:", "Keep abreast of others happenings", "Get behind on the news"),
    ("In phoning do you:", "Rarely question that it will all be said", "Rehearse what you’ll say"),
    ("In company do you:", "Start conversations", "Wait to be approached"),
    ("Does new and non-routine interaction with others:", "Stimulate and energize you", "Tax your reserves"),
    ("Do you prefer:", "Many friends with brief contact", "A few friends with longer contact"),
    ("Do you:", "Speak easily and at length with strangers", "Find little to say to strangers"),
    ("When the phone rings do you:", "Quickly get to it first", "Hope someone else will answer"),
    ("Are you more inclined to be:", "Easy to approach", "Somewhat reserved")]


questions2 = [("Are you more:", "Realistic", "Speculative"),
    ("Are you attracted to:", "Sensible people", "Imaginative people "),
    ("In doing ordinary things are you more likely to:", "Do it the usual way", "Do it your own way"),
    ("Facts:", "Speak for themselves", "Usually require interpretation"),
    ("Common sense is:", "Rarely questionable", "Frequently questionable"),
    ("Are you more frequently:", "A practical sort of person", "An abstract sort of person "),
    ("Do you go more by:", "Facts", "Principles"),
    ("Are you more likely to trust your:", "Experience", "Hunch"),
    ("Do you prize more in yourself:", "Good sense of reality", "Good imagination "),
    ("In writings do you prefer:", "The more literal", "The more figurative"),]
#Not in the MBTI questions list
questions3 = [("Is it worse to:", "Have your 'head in the clouds'", "Be 'in a rut'"),
    ("Are you more interested in:", "What is actual", "What is possible"),
    ("Writers should:", "'Say what they mean and mean what they say'", "Express things more by use of analogy"),
    ("Are visionaries:", "Somewhat annoying", "Rather fascinating"),
    ("Children often do not:", "Make themselves useful enough", "Exercise their fantasy enough"),
    ("Are you more likely to:", "See how others are useful", "See how others see"),
    ("Are you more interested in:", "Production and distribution", "Design and research"),
    ("Do you feel:", "More practical than ingenious", "More ingenious than practical"),
    ("Are you drawn more to:", "Fundamentals", "Overtones"),
    ("Is it harder for you to:", "Identify with others", "Utilize others")]

questions4 = [("Are you more impressed by:", "Principles", "Emotions"),
    ("In judging others are you more swayed by:", "Laws than circumstances", "Circumstances than laws"),
    ("Which appeals to you more:", "Consistency of thought", "Harmonious human relationships"),
    ("Are you inclined to be more:", "Cool headed", "Warm hearted"),
    ("In making decisions do you feel more comfortable with:", "Standards", "Feelings"),
    ("Which is more satisfying:", "To discuss an issue throughly", "To arrive at agreement on an issue"),
    ("Which is more of a compliment:", "There is a very logical person.", "There is a very sentimental person."),
    ("Are you typically more a person of:", "Clear reason", "Strong feeling"),
    ("Which seems the greater error:", "To be too passionate", "To be too objective"),
    ("Which do you wish more for yourself:", "Clarity of reason", "Strength of compassion")]

questions5 = [("Are more drawn toward the:", "Convincing", "Touching"),
    ("In first approaching others are you more:", "Objective and detached", "Personal and engaging"),
    ("Are you more comfortable in making:", "Logical judgments", "V alue judgments"),
    ("Is it worse to be:", "Unjust", "Merciless"),
    ("Are you more:", "Firm than gentle", "Gentle than firm"),
    ("Which rules you more:", "Your head", "Your heart"),
    ("Do you value in yourself more that you are:", "Unwavering", "Devoted"),
    ("Are you inclined more to be:", "Fair-minded", "Sympathetic"),
    ("Do you see yourself as basically:", "Hard-headed", "Soft-hearted"),
    ("Which is the greater fault:", "Being indiscriminate", "Being critical")]

questions6 = [("Do you prefer to work:", "To deadlines", "Just whenever"),
    ("Are you usually more:", "Punctual", "Leisurely"),
    ("Do you usually:", "Settle things", "Keep options open"),
    ("Should one usually let events occur:", "By careful selection and choice", "Randomly and by chance"),
    ("Which is more admirable:", "The ability to organize and be methodical", "The ability to adapt and make do"),
    ("Are you more comfortable with work:", "Contracted", "Done on a casual basis"),
    ("Do you more often prefer the:", "Final and unalterable statement", "Tentative and preliminary statement"),
    ("Is it preferable mostly to:", "Make sure things are arranged", "Just let things happen"),
    ("Which situation appeals to you more:", "The structured and scheduled", "The unstructured and unscheduled"),
    ("Do you prefer the:", "Planned events", "Unplanned event")]

questions7 = [("Do you tend to choose:", "Rather carefully", "Somewhat impulsively"),
    ("Does it bother you more having things:", "Incomplete", "Completed"),
    ("Would you say you are more:", "Serious and determined", "Easy-going"),
    ("Do you feel better about:", "Having purchased", "Having the option to buy"),
    ("Do you put more value on the:", "Definite", "Variable"),
    ("Do you tend to look for:", "The orderly", "Whatever turns up"),
    ("Are you more comfortable:", "After a decision", "Before a decision"),
    ("Is it your way more to:", "Get things settled", "Put off settlement"),
    ("Do you prefer to?:", "Set things up perfectly", "Allow things to come together"),
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
        st.text(key_c)
        my_bar.progress(15)
        pc_code = questions_print(questions2, key_c, 'S', 'N', 0, 0)
        if pc_code != None:
            #personality_code += pc_code[0]
            key_c += pc_code[1]
            #st.text(personality_code)
            st.text(key_c)
            my_bar.progress(30)
            pc_code = questions_print(questions3, key_c, 'S', 'N', pc_code[2], pc_code[3])
            if pc_code != None:
                personality_code += pc_code[0]
                key_c += pc_code[1]
                #st.text(personality_code)
                st.text(key_c)
                my_bar.progress(45)
                pc_code = questions_print(questions4, key_c, 'T', 'F', 0, 0)
                if pc_code != None:
                    #personality_code += pc_code[0]
                    key_c += pc_code[1]
                    #st.text(personality_code)
                    st.text(key_c)
                    my_bar.progress(60)
                    pc_code = questions_print(questions5, key_c, 'T', 'F', pc_code[2], pc_code[3])
                    if pc_code != None:
                        personality_code += pc_code[0]
                        key_c += pc_code[1]
                        #st.text(personality_code)
                        my_bar.progress(75)
                        st.text(key_c)
                        pc_code = questions_print(questions6, key_c, 'J', 'P', 0, 0)
                        if pc_code != None:
                            personality_code += pc_code[0]
                            key_c += pc_code[1]
                            #st.text(personality_code)
                            st.text(key_c)
                            my_bar.progress(90)
                            pc_code = questions_print(questions7, key_c, 'J', 'P', pc_code[2], pc_code[3])
                            if pc_code != None:
                                personality_code += pc_code[0]
                                key_c += pc_code[1]
                                st.text(personality_code)
                                st.text("Total number of questions answered"  + key_c)
                                my_bar.progress(100)
                                time.sleep(2)
                                placeholder6 =st.empty()
                                placeholder6.text("Congratulations! You have completed yoru MBTI test!")
                                st.balloons()
                                time.sleep(2)
                                placeholder6.empty()
                                test_complete = True
        if personality_code != "" and test_complete = True:
            st.header("Your MBTI is " + personality_code)
            if personality_code == "INFP":
                st.subheader(" The Mediator ")
                st.text("You can consider the following hobbie:")
                st.text("Poetry, creative writing, music, photography, theater, visual art")
            elif personality_code == "INFJ":
                st.subheader("The Advocate")
                st.text("You can consider the following hobbie:")
                st.text("Writing, art appreciation, reading, playing/listening to music, cooking/baking, crafting")
            elif personality_code == "ENFP":
                st.subheader("The Campaigner")
                st.text("You can consider the following hobbie:")
                st.text("Writing, creating art, playing instruments, listening to music, theater, reading fiction")
            elif personality_code == "ENFJ":
                st.subheader("The Protagonist")
                st.text("You can consider the following hobbie:")
                st.text("Reading, storytelling, cooking, writing, music, organizing events") 
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