import React from 'react';

function NavBar() {
    return (
        <div className="mainnav">
            <nav>
            <a href="/grid/p/site#r=home" className="headerlogo">
                <img src="logo.png" alt="Qb Prep"></img>
            </a>
            <a href="#Tutor-Services">Tutor-Services</a>
            <a href="#SAT">SAT</a>
            <a href="#GMAT">GMAT</a>
            <a href="#USMLE">USMLE</a>
            <a href="#Sign-In">Sign-In</a>
            <a href="#Register">Register</a>
            <input type="text" placeholder="Search..."></input>
            <button type="submit">Search</button>
            </nav>
        </div>
        
    )
}
export default NavBar;
