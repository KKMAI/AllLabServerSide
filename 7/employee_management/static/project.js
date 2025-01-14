function deleteProject(pro_id, csrf_token) {
  // กำหนด path ให้ถูกต้อง
  fetch(`/project2/${pro_id}/`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrf_token,
    },
  })
    .then(response => response.json())
    .then((data) => {
      console.log("Item deleted successfully");
      window.location.reload();
    })
    .catch((error) => console.error("Error:", error));
}