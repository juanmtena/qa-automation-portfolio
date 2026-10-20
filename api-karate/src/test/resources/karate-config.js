function fn() {
  var env = karate.env || 'dev';
  karate.configure('connectTimeout', 10000);
  karate.configure('readTimeout', 20000);
  return {
    env: env,
    baseUrl: 'https://restful-booker.herokuapp.com',
    username: 'admin',
    password: 'password123'
  };
}
