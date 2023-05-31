import { makeAutoObservable } from 'mobx';
import AuthService from '../services/AuthService';

export default class Store {
    isAuth = false;

    constructor() {
        makeAutoObservable(this);
    }

    setAuth(bool) {
        this.isAuth = bool;
    }

    async login(email, password) {
        try {
            const response = await AuthService.login(email, password);
            console.log(response);
            localStorage.setItem('token', response.data.access);
            this.setAuth(true);
        } catch (err) {
            console.log(err.response?.data?.message);
        }
    };

    async registration(username, email, password) {
        try {
            const response = await AuthService.registration(username, email, password);
            console.log(response);
            localStorage.setItem('token', response.data.access);
            this.setAuth(true);
        } catch (err) {
            console.log(err.response?.data?.message);
        }
    };
}