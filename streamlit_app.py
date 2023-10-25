import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
import os





load_css()

def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


col1, col2, col3 = st.columns(3)
col2.image(Image.open('kanhaiya.jpg'))

st.header('Kanhaiya Kumar Gupta')

st.info('I am a Computer Science student at IIIT Una with a strong background in Android Development, Competitive programming, and Problem-solving skills. I have experience in Golang for backend development. I have also actively contributed to the EUNOIA club, promoting literary and cultural activities at my university.')

st.markdown(
    """
## Highlights
"""
)

st.write("- Solve 350+ question on `Leetcode`", "[Link to Leetcode](https://leetcode.com/kanhaiyagupta/)")
st.write("- 1075 highest rating on `Codeforces`", "[Link to Codeforces](https://codeforces.com/profile/kanhaiyagupta9045)")
st.write("- I got placed `10550` rank out of `34000` candidates on `Educational Round Codeforces`")
st.write("- 1459 highest rating on `CodeChef`", "[Link to CodeChef](https://www.codechef.com/users/gupta_here)")
st.write("- Solve 270+ question on `GeeksForGeeks`", "[Link to GeeksForGeeks](https://auth.geeksforgeeks.org/user/kanhaiyarauniyar9045)")

st.markdown(
    """
## Education
"""
)

txt(
    " *Indian Institute of Information Technology*, Una, Himachal Pradesh",
    "2021-Present",
)
txt(
"- B. Tech. - **Computer Science and Engineering**",
"CGPA: **7.86**",
)


st.markdown(
        """
    ## Projects
    """
    )

col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Trello App")
    st.markdown("[Github](https://github.com/KanhaiyaKumarGupta/Trello)")

with col2:
    st.write("""
    I developed a Trello App for real-time task management. Users can assign tasks to multiple people and set deadlines. I used Kotlin, Firestore Database, and a Recycler View to create an efficient and visually pleasing app. It's a practical solution to enhance productivity and teamwork.
    """)
col3, col4 = st.columns([1, 3])

with col3:
    st.subheader("Real Time Chatting App")
    st.markdown("[Github](https://github.com/KanhaiyaKumarGupta/Real-Time-Chatting-App)")

with col4:
    st.write("""
  Real-time chatting app I developed using Kotlin and Firebase. This app has transformed communication by enabling instant and seamless conversations. I harnessed my skills in Kotlin to create a robust and responsive interface. Firebase Authentication ensured secure user access, while XML allowed for a user-friendly design. The integration of RecyclerView provided an organized and dynamic conversation interface. It's been a rewarding experience, knowing that this app has improved the way people interact and connect with each other.
    """)

col5, col6 = st.columns([1, 3])

with col5:
    st.subheader("Library Management")
    st.markdown("[Github](https://github.com/KanhaiyaKumarGupta/Library_Management)")

with col6:
    st.write("""
  I've have developed a Library Management System that streamlines the organization and management of library resources. My proficiency in HTML5, CSS, and JavaScript allowed me to create an intuitive and visually appealing user interface. Bootstrap added responsiveness and aesthetics to the system. Leveraging Node.js and Express.js, I ensured efficient server-side operations, and MongoDB handled data storage seamlessly. It was a rewarding project, knowing that it contributes to the efficient functioning of libraries, making resource management a breeze.
  """)




st.markdown(
        """
    ## Skills
    """
    )
txt3("Programming", "`Python`,`C`, `C++`, `Java`, `Golang`, `GIT`, `Linux`")
txt3("Developer Tools", "`GIT`, `Google-Colab`, `Anaconda`, `VSCode`, `AndroidStudio`, `Intellij Idea`")
txt3("Android Technologies", "`Kotlin`, `MVVM-Architecture`, `Retrofit`")
txt3("Web development", "`HTML`, `CSS`, `JavaScript`, `Node.js` `Express.js`, `Bootstrap`")
txt3("Databases", "`MySQL`, `Firebase`, `MongoDB`")
# txt3("Cloud Technology", "`AWS`")


icon_size = 20


st_button('', 'https://github.com/KanhaiyaKumarGupta/', 'Github', icon_size)
st_button('', 'https://www.linkedin.com/in/kanhaiya-kumar-gupta-550423228/', 'LinkedIn', icon_size)
st_button('', 'https://www.linkedin.com/in/kanhaiya-kumar-gupta-550423228/', 'LinkedIn', icon_size)
st_button('', 'https://www.instagram.com/kanhaiyagupta9045/', 'Instagram', icon_size)

