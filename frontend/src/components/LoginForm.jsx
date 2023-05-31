import React, { useContext, useState } from "react";
import { Context } from "..";


const LoginForm  = () => {
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const {store} = useContext(Context);

    return (
        <div>
            <input
                onChange={e => setEmail(e.target.value)}
                value={email}
                type="text"
                placeholder="Email"
        />
            <input
                onChange={e => setPassword(e.target.value)}
                value={password}
                type="text"
                placeholder="Password"
        />
            <input
                onChange={e => setUsername(e.target.value)}
                value={username}
                type="text"
                placeholder="Username"
        />


        <button onClick={() => store.login(email, password)}>
            Login
        </button>
        
        <button onClick={() => store.registration(username, email, password)}>
            Registration
        </button>
        </div>
    )
};

export default LoginForm;