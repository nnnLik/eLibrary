import axios from 'axios';

export const API_URL = 'http://localhost:8000';

const api = axios.create({
    withCredentials: true,
    baseURL: API_URL
})

api.interceptors.request.use((config) => {
    console.log(localStorage.getItem('token'));
    if (localStorage.getItem('token') != null) {
        config.headers.Authorization = `JWT ${localStorage.getItem('token')}`
        return config
    } else { return config }
})

export default api