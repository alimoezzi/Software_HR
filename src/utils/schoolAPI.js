import withQuery from 'with-query'

const api = "http://127.0.0.1:5000/api";
const login_url = "http://127.0.0.1:5000/login";
const logout_url = "http://127.0.0.1:5000/logout";
// var token = localStorage.token;
// var token = null;

const headers = (token)=>({
    Accept: "application/json",
    Host: "localhost:5000",
    authx: token
});

export const get = async (count, point, type, user_id=-1) => {
    try {
        var res = await fetch(withQuery(
            api + '/get',
            {
                type: type,
                count: count,
                point: point,
                user_id: user_id
            }
        ), { headers:headers(localStorage.getItem('access_token')) });
        var json = await res.json();
    } catch (e) {
        console.log(e);
    }

    return json;
};

export const add = async (type, object) => {
    try {
        var res = await fetch(withQuery(
            api + '/add',
            {
                type: type,
            }
        ), {
            method: "post",
            headers:headers(localStorage.getItem('access_token')),
            body: object
        });
        var json = await res.json();
    } catch (e) {
        console.log(e);
    }

    return json;
};

export const update = async (type, id, object) => {
    try {
        var res = await fetch(withQuery(
            api + '/update',
            {
                type: type,
                id:id
            }
        ), {
            method: "put",
            headers:headers(localStorage.getItem('access_token')),
            body: object
        });
        var json = await res.json();
    } catch (e) {
        console.log(e);
    }

    return json;
};

export const del = async (type, id) => {
    try {
        var res = await fetch(withQuery(
            api + '/del',
            {
                type: type,
            }
        ), {
            method: "DELETE",
            headers:headers(localStorage.getItem('access_token')),
            body: id
        });
        var json = await res.json();
    } catch (e) {
        console.log(e);
    }

    return json;
};

export const login = async (username, password) => {
    try {
        var res = await fetch(login_url, {
            method: "POST",
            headers:headers(localStorage.getItem('access_token')),
            body: JSON.stringify({
                username,
                password
            })
        }).then(r => r.json());
        var json = await res;
        console.log(res)
    } catch (e) {
        console.log(e);
    }
    if (json && json['access_token']) {
        localStorage.setItem('access_token','Bearer ' + json['access_token']);
    }
    return json;
};

export const logout = async () => {
    try {
        var res = await fetch(logout_url, {
            method: "GET",
            headers:headers(localStorage.getItem('access_token')),
        }).then(r => r.json());
        var json = await res;
        console.log(res)
    } catch (e) {
        console.log(e);
    }
    return json;
};

export const role = async () => {
    try {
        var res = await fetch(api + '/role', {
            headers:headers(localStorage.getItem('access_token')),
        }).then(r => r.json());
        var json = await res;
        console.log(res);
    } catch (e) {
        console.log(e);
    }
    return json;
};

export const move = async (from, item, to) => {
    try {
        var res = await fetch(withQuery(
            api + "/move",
            {
                from: from,
                item: item,
                to: to
            }
        ), { headers:headers(localStorage.getItem('access_token')) });
        var json = await res.json();
    } catch (e) {
        console.log(e);
    }
    return json;
};