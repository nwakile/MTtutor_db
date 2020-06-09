import React, { useState } from 'react';



function Login(props) {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    return (
        <div className="home">
            <div className="topContainer">
                <h2>Login</h2>
                <p>Sign into your Qb account</p>
                <input id="theInput1" placeholder="Email" onChange={e => setInputEmail(e.target.value)} />

                <input id="theInput2" placeholder="Password" onChange={e => setInputPassword(e.target.value)} />
                <br /> <br />
            </div>
            <div className="checkbox mb-3">
                <label>
                    Remember me
                    <input type="checkbox" value="remember-me" />
                </label>
                <button id="theButton3">Login</button> <br /> <br />
                <a href="reset_password/newpassword.html">Forgot your password?</a>
                <p>email: {inputEmail}</p>
                <p>password: {inputPassword}</p>
            </div>

        </div>
        
    );
}


function Login(props) {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const getLoginId = async () => {

        const response = await fetch("http://localhost:5000/userlogin");

        const inputEmail = await response.json();
        const inputPassword = await response.json();

        console.log(inputEmail);

        setInputEmail(inputEmail);

        return inputEmail;
      }
    
      return (

        <button onClick={getLoginId}>Get Login Id</button>

      )
    }
    

export default Login;
