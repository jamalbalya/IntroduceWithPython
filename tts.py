import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',130)
engine.say("Hello Greeting, this is sample speak with python programming language")
engine.say("in this session i want to give short introduce on me")
engine.say("I am writing to you to express my interest in your company. With 6 years of experience as a Banking Consultant, 3+ years of experience in a Retail company on IT Corporate, and from 2020 until now in a software house company as an IT Quality Assurance Manager, My responsibilities have Included the IT Quality Assurance and Technical Writer team separate in two areas Bandung and Bali. Experience has taught me how to build strong relationships with all departments in the organization. I can work within a team as well as cross-team. I can work with engineers to resolve technical issues and implement technical enhancements, work with the development department to implement design and functional enhancements, and monitor.")
engine.say("that's a short introducing about me, if you have any question please feel free to contact to related CV that i give you before, thank you very much for you attention. Best Regards. Jamal Balya")
engine.runAndWait()
engine.stop()
