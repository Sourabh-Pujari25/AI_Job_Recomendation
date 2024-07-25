import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
def main():
   
    
    # Main column for user input/output
    col1, col2, col3 = st.columns([1.5, 5, 1.5])

    with col1:
        option = st.selectbox("Select an option", ["I want to be", "I am skilled in", "Chat with AI"])
    with col2:
        user_input = st.text_input("Enter your input here")
        
    with col3:
        st.markdown('<div style="height:27px;visibility:hidden;"></div>',unsafe_allow_html=True)
        st.button("Submit",use_container_width=True,type="primary")
      

        
    # Artificial Intelligence (AI) Job Roles
    ai_job_roles = [
        # Junior/Fresher Level
        "AI Intern",
        "AI Trainee",
        "Junior AI Developer",
        "AI Research Assistant",

        # Mid-Level
        "AI Engineer",
        "Machine Learning Engineer",
        "AI Software Developer",
        "Natural Language Processing (NLP) Engineer",
        "Computer Vision Engineer",

        # Senior Level
        "AI Team Lead",
        "AI Architect",
        "Senior AI Researcher",
        "Principal AI Scientist",
        "Chief AI Officer (CAIO)"
    ]

    # Machine Learning (ML) Job Roles
    ml_job_roles = [
        # Junior/Fresher Level
        "ML Intern",
        "ML Trainee",
        "Junior ML Engineer",
        "Data Analyst (with ML focus)",

        # Mid-Level
        "Machine Learning Developer",
        "ML Modeler",
        "Data Scientist (with ML specialization)",
        "ML Operations (MLOps) Engineer",

        # Senior Level
        "ML Team Lead",
        "ML Architect",
        "Senior Data Scientist",
        "Principal ML Engineer",
        "Chief Data Officer (CDO)"
    ]

    # Python Job Roles (in AI/ML context)
    python_job_roles = [
        # Junior/Fresher Level
        "Python Developer (with AI/ML interest)",
        "Junior Data Analyst (Python proficient)",
        "Automation Tester (Python)",

        # Mid-Level
        "Python Software Engineer",
        "Data Engineer (Python)",
        "Python Data Analyst",
        "Python Backend Developer (AI/ML applications)",

        # Senior Level
        "Python Technical Lead",
        "Senior Python Developer (AI/ML focus)",
        "Python Solutions Architect",
        "Chief Technology Officer (CTO) with Python expertise"
    ]

    # Additional Specialized Roles
    specialized_roles = [
        "AI Ethics Specialist",
        "AI Product Manager",
        "AI Business Analyst",
        "AI Consultant",
        "AI Infrastructure Engineer"
    ]

    data=pd.read_excel("Database/Job_Roles.xlsx")

    # data_columns = data.columns
    data_columns = ['Domain', 'Level', 'Job Roles']
    list_jobs_domain=data['Domain'].to_list()
    list_jobs_Level=data['Level'].to_list()
    list_jobs_roles=data['Job Roles'].to_list()


    job_titles=[ai_job_roles,ml_job_roles,python_job_roles,specialized_roles]
    for i in job_titles:
        columns_display(i)


    

def card(job_name):
    st.markdown("""<style>.card p {
  font-size: 17px;
  font-weight: 400;
  line-height: 20px;
  color: #666;
}

.card p.small {
  font-size: 14px;
}

.go-corner {
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  width: 32px;
  height: 32px;
  overflow: hidden;
  top: 0;
  right: 0;
  background-color: #00838d;
  border-radius: 0 4px 0 32px;
}

.go-arrow {
  margin-top: -4px;
  margin-right: -4px;
  color: white;
  font-family: courier, sans;
}

.card1 {
  display: block;
  position: relative;
  max-width: 262px;
  background-color: #f2f8f9;
  border-radius: 4px;
  padding: 32px 24px;
  margin: 12px;
  text-decoration: none;
  z-index: 0;
  overflow: hidden;
}

.card1:before {
  content: "";
  position: absolute;
  z-index: -1;
  top: -16px;
  right: -16px;
  background: #00838d;
  height: 32px;
  width: 32px;
  border-radius: 32px;
  transform: scale(1);
  transform-origin: 50% 50%;
  transition: transform 0.25s ease-out;
}

.card1:hover:before {
  transform: scale(21);
}

.card1:hover p {
  transition: all 0.3s ease-out;
  color: rgba(255, 255, 255, 0.8);
}

.card1:hover h3 {
  transition: all 0.3s ease-out;
  color: #fff;
}

.card2 {
  display: block;
  top: 0px;
  position: relative;
  max-width: 262px;
  background-color: #f2f8f9;
  border-radius: 4px;
  padding: 32px 24px;
  margin: 12px;
  text-decoration: none;
  z-index: 0;
  overflow: hidden;
  border: 1px solid #f2f8f9;
}

.card2:hover {
  transition: all 0.2s ease-out;
  box-shadow: 0px 4px 8px rgba(38, 38, 38, 0.2);
  top: -4px;
  border: 1px solid #ccc;
  background-color: white;
}

.card2:before {
  content: "";
  position: absolute;
  z-index: -1;
  top: -16px;
  right: -16px;
  background: #00838d;
  height: 32px;
  width: 32px;
  border-radius: 32px;
  transform: scale(2);
  transform-origin: 50% 50%;
  transition: transform 0.15s ease-out;
}

.card2:hover:before {
  transform: scale(2.15);
}

.card3 {
  display: block;
  top: 0px;
  position: relative;
  max-width: 262px;
  background-color: #f2f8f9;
  border-radius: 4px;
  padding: 32px 24px;
  margin: 12px;
  text-decoration: none;
  overflow: hidden;
  border: 1px solid #f2f8f9;
}

.card3 .go-corner {
  opacity: 0.7;
}

.card3:hover {
  border: 1px solid #00838d;
  box-shadow: 0px 0px 999px 999px rgba(255, 255, 255, 0.5);
  z-index: 500;
}

.card3:hover p {
  color: #00838d;
}

.card3:hover .go-corner {
  transition: opactiy 0.3s linear;
  opacity: 1;
}

.card4 {
  display: block;
  top: 0px;
  position: relative;
  max-width: 262px;
  background-color: #fff;
  border-radius: 4px;
  padding: 32px 24px;
  margin: 12px;
  text-decoration: none;
  overflow: hidden;
  border: 1px solid #ccc;
}

.card4 .go-corner {
  background-color: #00838d;
  height: 100%;
  width: 16px;
  padding-right: 9px;
  border-radius: 0;
  transform: skew(6deg);
  margin-right: -36px;
  align-items: start;
  background-image: linear-gradient(-45deg, #8f479a 1%, #dc2a74 100%);
}

.card4 .go-arrow {
  transform: skew(-6deg);
  margin-left: -2px;
  margin-top: 9px;
  opacity: 0;
}

.card4:hover {
  border: 1px solid #cd3d73;
}

.card4 h3 {
  margin-top: 8px;
}

.card4:hover .go-corner {
  margin-right: -12px;
}

.card4:hover .go-arrow {
  opacity: 1;
}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<html><div class="card">
   <a class="card1" href="#">
    <p>{job_name}</p>
    # <p class="small">Card description with lots of great facts and interesting details.</p>
    <div class="go-corner" href="#">
      <div class="go-arrow">
        →
      </div>
    </div>
  </a>
</div></html>""",unsafe_allow_html=True)
    
def columns_display(list_jobs):
    num_columns = 4
    num_per_col = len(list_jobs) // num_columns

    columns = st.columns(num_columns)
    for i in range(num_columns):
        with columns[i]:
            for j in range(num_per_col):
                index = i * num_per_col + j
                if index < len(list_jobs):
            
                    card(list_jobs[index])
                    #st.button(list_jobs[index])



    
if __name__=="__main__":
    main()