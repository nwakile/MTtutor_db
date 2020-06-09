import React from 'react';


function Questions(props) {
    return (
        <div className="home">

            <div class="topContainer">
                <h5>Question 1 of 10</h5>
                <h5>QuestionId: 14 </h5>
                <p>
                    "A 62-year-old woman is evaluated during a follow-up appointment 12 weeks after she completed treatment for
                    genotype 1a hepatitis C virus (HCV) infection. She has Child-Turcotte-Pugh Class A cirrhosis
                    (well-compensated cirrhosis). Small esophageal varices were noted on upper endoscopy 1 year earlier.
                    On physical examination, vital signs are normal; BMI is 26. Palmar erythema, spider angiomata over the
                    chest, a firm liver edge 3 cm below the costal margin, and a palpable spleen tip are noted. The examination
                    is otherwise normal.
                    Her HCV RNA is undetectable and her calculated Model for End-Stage Liver Disease score is 8. Which of the
                    following is the most appropriate management for this patient?"
                </p>

            </div>
            <div className="midContainer">
                <form action="">
                    <input type="radio" name="gender" value="A. " />A. Liver transplantation evaluation <br />
                    <input type="radio" name="gender" value="B. " />B. Measurement of HCV RNA in 12 weeks <br />
                    <input type="radio" name="gender" value="B. " />C. Ultrasonography of the liver every 6 months <br />
                    <input type="radio" name="gender" value="D. " />D. Upper Endoscopy <br />
                    <input type="radio" name="gender" value="E. " />E. None of the above <br />
                </form>
            </div>
            <br /> <br />

        </div>

    );
}

export default Questions;
