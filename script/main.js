function openModal()
{
    const modal = document.getElementById("myModal");
    const button = document.getElementById("modalButton");
    const close = document.getElementsByClassName("close")[0];

    // Toon de modal wanneer op de knop wordt geklikt
    button.onclick = function()
    {
        modal.style.display = "block";
    }

    // Sluit de modal wanneer op het 'sluiten' icoon wordt geklikt
    close.onclick = function() 
    {
        modal.style.display = "none";
    }

    // Sluit de modal wanneer buiten de modal wordt geklikt
    window.onclick = function(event) 
    {
        if (event.target == modal) 
        {
            modal.style.display = "none";
        }
    }
}