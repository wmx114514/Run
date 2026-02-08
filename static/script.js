const loginBtn = document.getElementById("loginBtn");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const msgEl = document.getElementById("msg");

loginBtn.addEventListener("click", async () => {
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  if (!username || !password) {
    msgEl.textContent = "请输入账号和密码";
    return;
  }

  try {
    const res = await fetch("http://127.0.0.1:5000/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    if (data.code === 0) {
      msgEl.textContent = "";
      // 保存用户名到本地存储
      localStorage.setItem("username", data.username);
      localStorage.setItem("role", data.role);

      // 根据角色跳转
      if (data.role === "admin") {
        window.location.href = "./admin/admin.html";
      } else {
        window.location.href = "./user.html";
      }
    } else {
      msgEl.textContent = data.msg;
    }
  } catch (err) {
    msgEl.textContent = "网络错误，请检查后端是否启动";
    console.error(err);
  }
});
