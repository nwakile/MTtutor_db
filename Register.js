import React, { useState } from 'react';

  
function Register(props) {
    const [inputFirstName, setInputFirstName] = useState("");
    const [inputLastName, setInputLastName] = useState("");
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const [inputConfirmpassword, setInputConfirmpassword] = useState("");
    return (
        <div className="home">

            <div className="topContainer">
                <h2>Register</h2>
                <input id="theInput1" placeholder="FirstName" onChange={e => setInputFirstName(e.target.value)} />
                <input id="theInput2" placeholder="LastName" onChange={e => setInputLastName(e.target.value)} />
                <br /> <br />
                <input id="theInput3" placeholder="Email" onChange={e => setInputEmail(e.target.value)} />
                <br /> <br />
                <input id="theInput4" placeholder="Password" onChange={e => setInputPassword(e.target.value)} />
                <input id="theInput5" placeholder="Confirmpassword" onChange={e => setInputConfirmpassword(e.target.value)} />
                <br /> <br />
                <button id="theButton1">Register</button> <br /> <br />
                <p>First Name: {inputFirstName}</p>
                <p>Last Name: {inputLastName}</p>
                <p>Email: {inputEmail}</p>
                <p>Password: {inputPassword}</p>
                <p>Confirm password: {inputConfirmpassword}</p>

            </div>

        </div>


    );
}


export default Register;
