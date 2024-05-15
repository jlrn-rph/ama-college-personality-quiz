import streamlit as st

def recommend_program(answers):
    score = {
        "Information Technology": 0,
        "Computer Science": 0,
        "Artificial Intelligence": 0,
        "Data Science": 0,
        "Cybersecurity": 0,
        "Blockchain": 0,
    }

    if answers['enjoy_math_problems'] == "Yes":
        score["Computer Science"] += 1
        score["Artificial Intelligence"] += 3  
        score["Data Science"] += 2
    
    if answers['tech_gadgets'] == "Yes":
        score["Information Technology"] += 2
        score["Artificial Intelligence"] += 1  
        score["Blockchain"] += 1
        score["Cybersecurity"] += 1
    
    if answers['coding'] == "Yes":
        score["Computer Science"] += 2
        score["Artificial Intelligence"] += 2  
        score["Data Science"] += 1
        score["Cybersecurity"] += 1
        score["Blockchain"] += 1
    
    if answers['analyzing_data'] == "Yes":
        score["Data Science"] += 3
        score["Artificial Intelligence"] += 2 
    
    if answers['security_concerns'] == "Yes":
        score["Cybersecurity"] += 3
    
    if answers['blockchain_interest'] == "Yes":
        score["Blockchain"] += 3
    
    if answers['solving_problems'] == "Yes":
        score["Artificial Intelligence"] += 3  
        score["Computer Science"] += 1
        score["Data Science"] += 1
    
    if answers['gaming'] == "Yes":
        score["Computer Science"] += 1
        score["Artificial Intelligence"] += 2  
        score["Information Technology"] += 1
    
    if answers['online_shopping'] == "Yes":
        score["Blockchain"] += 1
        score["Cybersecurity"] += 1
        score["Data Science"] += 1
    
    if answers['social_media'] == "Yes":
        score["Information Technology"] += 2
        score["Data Science"] += 1
        score["Artificial Intelligence"] += 1  

    recommended_program = max(score, key=score.get)
    return recommended_program

program_info = {
    "Information Technology": {
        "description": "Hey there! Welcome to the world of Information Technology (Information Technology)! If you're anything like Athena, you love creating intelligent solutions that help businesses thrive. In this program, you'll dive into network management, system administration, software development, and database management.",
        "learning": "You'll be learning how to manage networks, develop software, and work with databases.",
        "tools": "You'll get hands-on experience with Cisco networking tools, Microsoft Azure, AWS, and SQL databases.",
        "roles": "Upon graduation, you can become an Information Technology Support Specialist, Network Administrator, System Administrator, or even an Information Technology Manager!",
        "persona": "Athena",
        "persona_desc": "She's into creating intelligent solutions that help businesses thrive. She loves diving into network management, system administration, software development, and database management.",
    },
    "Computer Science": {
        "description": "Hey there! Welcome to the exciting world of Computer Science (Computer Science)! If you're anything like Ethan, you're passionate about diving deep into the theoretical foundations of computing and software development. Get ready to explore algorithms, data structures, and software engineering!",
        "learning": "In this program, you'll learn about algorithms, data structures, software engineering, operating systems, and computer architecture.",
        "tools": "You'll get to use programming languages like Java, C++, Python, and tools like Git and Unix/Linux.",
        "roles": "Upon graduation, you can become a Software Developer, Systems Analyst, Computer Scientist, or even a Research Scientist!",
        "persona": "Ethan",
        "persona_desc": "He enjoys diving deep into the theoretical foundations of computing and loves to develop software solutions. He's passionate about algorithms, data structures, and software engineering.",
    },
    "Artificial Intelligence": {
        "description": "Hey there! Welcome to the world of Artificial Intelligence (Artificial Intelligence)! If you're anything like Liam, you're fascinated by creating intelligent systems that can learn and make decisions. Get ready to dive into machine learning, neural networks, natural language processing, and more!",
        "learning": "In this program, you'll explore machine learning, neural networks, natural language processing, robotics, and computer vision.",
        "tools": "You'll work with tools like TensorFlow, Keras, PyTorch, Python, R, and MATLAB.",
        "roles": "Upon graduation, you can become an Artificial Intelligence Engineer, Machine Learning Engineer, Data Scientist, or even a Research Scientist in Artificial Intelligence!",
        "persona": "Liam",
        "persona_desc": "He's fascinated by creating intelligent systems that can learn and make decisions. He's diving deep into machine learning, neural networks, natural language processing, robotics, and computer vision.",
    },
    "Data Science": {
        "description": "Hey there! Welcome to the world of Data Science! If you're anything like Sophia, you love exploring and extracting insights from data. Get ready to dive into statistics, machine learning, data mining, and big data technologies!",
        "learning": "In this program, you'll learn about statistics, machine learning, data mining, big data technologies, and data visualization.",
        "tools": "You'll use tools like Python, R, SQL, Hadoop, Spark, and Tableau to analyze and visualize data.",
        "roles": "Upon graduation, you can become a Data Scientist, Data Analyst, Business Analyst, or even a Data Engineer!",
        "persona": "Sophia",
        "persona_desc": "She loves exploring and extracting insights from data. She's diving deep into statistics, machine learning, data mining, big data technologies, and data visualization.",
    },
    "Cybersecurity": {
        "description": "Hey there! Welcome to the world of Cybersecurity! If you're anything like Noah, you're passionate about protecting systems and networks from cyber threats. Get ready to dive into network security, cryptography, ethical hacking, and more!",
        "learning": "In this program, you'll learn about network security, cryptography, ethical hacking, risk management, and information assurance.",
        "tools": "You'll work with tools like firewalls, intrusion detection systems, encryption tools, and penetration testing tools.",
        "roles": "Upon graduation, you can become a Cybersecurity Analyst, Security Consultant, Ethical Hacker, or even an Information Security Manager!",
        "persona": "Noah",
        "persona_desc": "He's passionate about protecting systems and networks from cyber threats. He's learning about network security, cryptography, ethical hacking, risk management, and information assurance.",
                "persona_desc": "He's passionate about protecting systems and networks from cyber threats. He's learning about network security, cryptography, ethical hacking, risk management, and information assurance.",
    },
    "Blockchain": {
        "description": "Hey there! Welcome to the world of Blockchain! If you're anything like Olivia, you're fascinated by blockchain technology and its potential applications. Get ready to dive into cryptography, blockchain architecture, smart contracts, and decentralized applications (dApps)!",
        "learning": "In this program, you'll learn about cryptography, blockchain architecture, smart contracts, and decentralized applications (dApps).",
        "tools": "You'll work with tools like Ethereum, Hyperledger, Solidity, Truffle, and Ganache to develop blockchain solutions.",
        "roles": "Upon graduation, you can become a Blockchain Developer, Blockchain Consultant, Smart Contract Developer, or even a Blockchain Architect!",
        "persona": "Olivia",
        "persona_desc": "She's fascinated by blockchain technology and its potential applications. She's learning about cryptography, blockchain architecture, smart contracts, and decentralized applications (dApps).",
    }
}

def main():
    st.set_page_config(page_title="College Program Recommender", page_icon="🎓")

    st.image("assets/main-header.jpg")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Personality Quiz", "About"))

    if page == "Personality Quiz":
        personality_quiz()

    elif page == "About":
        about_page()

def personality_quiz():
    st.write("Welcome! Let's find the perfect college program for you.")

    user_name = st.text_input("What's your name?")
    if user_name:
        st.write(f"Hello, {user_name}! Let's get started with the personality quiz.")

        answers = {}

        answers['enjoy_math_problems'] = st.radio("Do you enjoy solving math problems, like algebra and trigonometry?", ["Yes", "No"])
        answers['tech_gadgets'] = st.radio("Are you always excited about the latest tech gadgets and apps?", ["Yes", "No"])
        answers['coding'] = st.radio("Do you enjoy coding, such as creating websites or mobile apps?", ["Yes", "No"])
        answers['analyzing_data'] = st.radio("Do you like analyzing data to uncover patterns, like working with Excel or Google Sheets?", ["Yes", "No"])
        answers['security_concerns'] = st.radio("Are you concerned about online security and enjoy learning how to protect against cyber threats?", ["Yes", "No"])
        answers['blockchain_interest'] = st.radio("Are you fascinated by blockchain technology and cryptocurrencies like Bitcoin?", ["Yes", "No"])
        answers['solving_problems'] = st.radio("Do you enjoy solving complex problems and puzzles?", ["Yes", "No"])
        answers['gaming'] = st.radio("Do you love playing video games and are interested in how they are made?", ["Yes", "No"])
        answers['online_shopping'] = st.radio("Do you frequently shop online and are interested in how e-commerce platforms work?", ["Yes", "No"])
        answers['social_media'] = st.radio("Are you active on social media and interested in how these platforms function?", ["Yes", "No"])

        if st.button('Get My Recommendation!'):
            st.image("assets/recommendation.jpg")
            program = recommend_program(answers)
            info = program_info[program]
            st.write(f"Based on your answers, you're like {info['persona']}! {info['persona_desc']}")
            st.write(f"### {program} Program Overview")
            st.write(f"{info['description']}")
            st.write(f"**What you will learn:** {info['learning']}")
            st.write(f"**Tools typically used:** {info['tools']}")
            st.write(f"**Potential job roles upon graduation:** {info['roles']}")

def about_page():
    st.title("About")
    st.write("Welcome to the College of Computer Studies at AMA University! Our college offers a range of innovative and industry-relevant programs designed to prepare students for exciting careers in technology. Here are some of the programs we offer:")

    st.write("### Bachelor of Science in Information Technology (BSIT)")
    st.write("Our BSIT program equips students with a comprehensive understanding of information technology concepts and applications. Graduates are prepared for roles such as IT support specialists, network administrators, and system analysts.")

    st.write("### Bachelor of Science in Computer Science (BSCS)")
    st.write("The BSCS program focuses on computer science fundamentals, software development, and system analysis. Students develop strong problem-solving skills and are prepared for careers as software developers, computer scientists, and research analysts.")

    st.write("### Bachelor of Science in Data Science (BSDS)")
    st.write("In our BS Data Science program, students learn how to extract insights from data, apply statistical analysis techniques, and develop machine learning models. Graduates are in high demand for roles such as data scientists, data analysts, and business intelligence specialists.")

    st.write("### Bachelor of Science in Cybersecurity (BSCyBS)")
    st.write("Cybersecurity is a critical field in today's digital age. Our BS Cybersecurity program covers topics such as network security, cryptography, ethical hacking, and risk management. Graduates are prepared to defend organizations against cyber threats as cybersecurity analysts, consultants, and information security managers.")

    st.write("### Bachelor of Science in Blockchain (BSBT)")
    st.write("Blockchain technology is revolutionizing various industries, from finance to healthcare. Our BS Blockchain program explores the principles of blockchain architecture, smart contracts, and decentralized applications. Graduates can pursue careers as blockchain developers, consultants, and architects.")

    st.write("### Bachelor of Science in Artificial Intelligence (BSAI)")
    st.write("AI is transforming the way we live and work. Our BS AI program focuses on machine learning, neural networks, natural language processing, and robotics. Graduates are at the forefront of AI innovation, working as AI engineers, machine learning specialists, and research scientists.")

    st.write("### Why Choose AMA University College of Computer Studies?")
    st.write("1. Industry-Relevant Curriculum: Our programs are designed in collaboration with industry experts to ensure that students learn the latest technologies and skills demanded by employers.")
    st.write("2. Experienced Faculty: Our faculty members are experienced professionals with expertise in their respective fields, providing students with valuable insights and guidance.")
    st.write("3. State-of-the-Art Facilities: Students have access to cutting-edge technology labs, software, and resources to support their learning and research.")
    st.write("4. Career Opportunities: With our strong industry connections and internship programs, students have access to a wide range of career opportunities and practical experiences.")
    st.write("5. Student Support: We provide comprehensive academic and career support services to help students succeed in their academic journey and transition into the workforce.")

    st.write("Join us at the College of Computer Studies, where you'll receive quality education, hands-on experience, and preparation for a successful career in the dynamic field of technology! Inquire at https://forms.gle/mbR1MqvjsXGNpgwu7 and our admission officer will contact you to provide more info.")
    st.image("assets/ama-enroll.jpg")
    st.image("assets/ama-enroll1.jpg")



if __name__ == "__main__":
    main()