import api from '../http';

export default class AuthService {
    static async login(email, password) {
        return api.post('/auth/jwt/create/', { email, password })
    }

    static async registration(username, email, password) {
        console.log(username, email, password);
        return api.post('/auth/users/', { username, email, password })
    }
}