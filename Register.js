import React, { useState } from 'react';

  
function Register(props) {
    const [inputUsername, setInputUsername] = useState("");
    const [inputPhone, setInputPhone] = useState("");
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const [inputConfirmpassword, setInputConfirmpassword] = useState("");
    const getSignup = async () => {

        const configs = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: inputUsername, phone: inputPhone, email: inputEmail, password: inputPassword, confirmpassword: inputConfirmpassword}),
            mode: 'cors'
        }

        const response = await fetch("http://localhost:5000/app/create", configs);
        const data = await response.json();
        console.log(data);
        // setAuthToken(data.token)
      }
    return (
        <div className="home">

            <div className="topContainer">
                <h2>Register</h2>
                <input id="theInput1" placeholder="Username" onChange={e => setInputUsername(e.target.value)} />
                <input id="theInput2" placeholder="Phone" onChange={e => setInputPhone(e.target.value)} />
                <br /> <br />
                <input id="theInput3" placeholder="Email" onChange={e => setInputEmail(e.target.value)} />
                <br /> <br />
                <input id="theInput4" placeholder="Password" onChange={e => setInputPassword(e.target.value)} />
                <input id="theInput5" placeholder="Confirmpassword" onChange={e => setInputConfirmpassword(e.target.value)} />
                <br /> <br />
                <button id="theButton1" onClick={getSignup}>Register</button> <br /> <br />
                <p>Username: {inputUsername}</p>
                <p>Phone: {inputPhone}</p>
                <p>Email: {inputEmail}</p>
                <p>Password: {inputPassword}</p>
                <p>Confirm password: {inputConfirmpassword}</p>

            </div>

        </div>


    );
}


export default Register;
