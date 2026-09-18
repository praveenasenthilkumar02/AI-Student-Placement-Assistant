import os
from dotenv import load_dotenv
from groq import Groq


# ============================================================
# 1. LOAD API KEY
# ============================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ API key not found!")
    print("Please check your .env file.")
    exit()


# ============================================================
# 2. CREATE GROQ CLIENT
# ============================================================

try:
    client = Groq(api_key=api_key)
except Exception as e:
    print("❌ Failed to create Groq client")
    print(e)
    exit()


# ============================================================
# 3. PROMPT ENGINEERING
# ============================================================

SYSTEM_PROMPT = """
You are an AI Student Placement Assistant.

Your main purpose is to help college students prepare
for campus placements.

You have four modules.

MODULE 1 - APTITUDE AND REASONING

Help students with:
- Quantitative aptitude
- Percentages
- Profit and loss
- Time and work
- Ratio and proportion
- Logical reasoning
- Verbal ability
- Practice questions
- Step-by-step solutions

MODULE 2 - TECHNICAL INTERVIEW

Help students with:
- Python
- Java
- C
- SQL
- DBMS
- OOP
- Data Structures
- Operating Systems
- Computer Networks
- Coding questions
- Technical interview questions
- Simple explanations

MODULE 3 - HR INTERVIEW

Help students with:
- Self introduction
- Strengths and weaknesses
- Career goals
- Common HR questions
- Mock interviews
- Communication improvement
- Answer feedback

During mock interviews:
- Ask only one question at a time.
- Wait for the student's answer.
- Give feedback.
- Then ask the next question.

MODULE 4 - RESUME AND CAREER GUIDANCE

Help students with:
- Resume improvement
- Skills suggestions
- Project ideas
- Career roadmap
- Job role guidance
- Placement preparation strategy
- Interview preparation

GENERAL RULES:

1. Give simple and clear answers.
2. Explain difficult concepts step by step.
3. Use examples whenever useful.
4. Keep answers focused on placements.
5. Encourage the student.
6. Correct mistakes politely.
7. Do not make up information.
8. If the question is unrelated to placements,
   politely say that you are a Student Placement Assistant.
"""


# ============================================================
# 4. AI RESPONSE FUNCTION
# ============================================================

def ask_ai(module, user_question, conversation):

    prompt = f"""
The student is currently using:

MODULE:
{module}

Student Question:
{user_question}

Answer according to the selected module.

Give a simple, practical and placement-focused response.
"""

    try:

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # Add previous conversation
        messages.extend(conversation)

        # Add current user question
        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = client.chat.completions.create(

            # Working model confirmed from your API
            model="openai/gpt-oss-20b",

            messages=messages,

            temperature=0.7,

            max_tokens=600
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"""
❌ API ERROR

{e}

Please check your internet connection and API access.
"""


# ============================================================
# 5. MAIN MENU
# ============================================================

def show_menu():

    print("\n" + "=" * 65)

    print("          🎓 AI STUDENT PLACEMENT ASSISTANT")

    print("=" * 65)

    print("""
Choose a module:

1. 📚 Aptitude & Reasoning
2. 💻 Technical Interview
3. 🗣️ HR Interview
4. 📄 Resume & Career Guidance

Type 'exit' to close the chatbot.
""")


# ============================================================
# 6. START CHATBOT
# ============================================================

print("\n🚀 Starting AI Student Placement Assistant...")

print("✅ API Key loaded")
print("✅ Groq API connected")
print("✅ AI Model: openai/gpt-oss-20b")
print("✅ Chatbot ready!")


# ============================================================
# 7. MAIN LOOP
# ============================================================

while True:

    show_menu()

    choice = input("👩‍🎓 Select Module (1-4): ").strip()


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if choice.lower() == "exit":

        print("\n" + "=" * 65)

        print("🤖 AI: Thank you for using the Placement Assistant!")

        print("🎯 Good luck with your placements!")

        print("=" * 65)

        break


    # --------------------------------------------------------
    # MODULE SELECTION
    # --------------------------------------------------------

    if choice == "1":

        module = "Aptitude and Reasoning"

        icon = "📚"

    elif choice == "2":

        module = "Technical Interview"

        icon = "💻"

    elif choice == "3":

        module = "HR Interview"

        icon = "🗣️"

    elif choice == "4":

        module = "Resume and Career Guidance"

        icon = "📄"

    else:

        print("\n❌ Invalid choice!")

        print("Please select 1, 2, 3 or 4.")

        continue


    # ========================================================
    # MODULE START
    # ========================================================

    print("\n" + "=" * 65)

    print(f"{icon} {module.upper()}")

    print("=" * 65)

    print("Type 'back' to return to the main menu.")

    print("Type 'exit' to close the chatbot.")

    print()


    # Conversation memory
    conversation = []


    # ========================================================
    # CHAT LOOP
    # ========================================================

    while True:

        user_input = input("👩‍🎓 You: ").strip()


        # ----------------------------------------------------
        # BACK
        # ----------------------------------------------------

        if user_input.lower() == "back":

            print("\n↩️ Returning to main menu...")

            break


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        if user_input.lower() == "exit":

            print("\n🤖 AI: Good luck with your placements! 🎯")

            exit()


        # ----------------------------------------------------
        # EMPTY INPUT
        # ----------------------------------------------------

        if not user_input:

            print("⚠️ Please enter your question.")

            continue


        # ----------------------------------------------------
        # AI RESPONSE
        # ----------------------------------------------------

        print("\n🤖 AI:")

        answer = ask_ai(
            module,
            user_input,
            conversation
        )

        print(answer)


        # ----------------------------------------------------
        # SAVE CONVERSATION
        # ----------------------------------------------------

        conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        conversation.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        print()