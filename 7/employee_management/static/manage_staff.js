function addStaff(pro_id, csrf_token){
    const emp = document.getElementById('input-add-staff');
    const data = {emp_id: emp.value};
    
    // กำหนด path ให้ถูกต้อง
    fetch(`/project2/detail/${pro_id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}


async function removeStaff(pro_id, emp_id, csrf_token){
    // กำหนด path ให้ถูกต้อง
    fetch(`/project2/detail/${pro_id}/${emp_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    })
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}