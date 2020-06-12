import React, { useState } from 'react';



function Login(props) {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const getLoginId = async () => {

        const configs = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({email: inputEmail, password: inputPassword}),
            mode: 'cors'
        }

        const response = await fetch("http://localhost:5000/app/login", configs);
        const data = await response.json();
        console.log(data);
        // setAuthToken(data.token)
      }

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
                <button id="theButton3" onClick={getLoginId}>Login</button> <br /> <br />
                <a href="reset_password/newpassword.html">Forgot your password?</a>
                <p>email: {inputEmail}</p>
                <p>password: {inputPassword}</p>
            </div>

        </div>
        
    );
}



export default Login;
