document.addEventListener("DOMContentLoaded", () => {
    const teamMembersContainer = document.getElementById('team-members-container');

    fetch('static/data/team-members.JSON')
        .then(response => response.json())
        .then(data => {
            const teams = {
                "captains": "Captains",
                "software": "Software Team",
                "mechanical": "Mechanical Team",
                "electrical": "Electrical Team",
                "media": "Media Team",
                "community": "Community Team",
                "mentors": "Mentors"
            };

            for (let team in teams) {
                const section = document.createElement('section');
                const title = document.createElement('h2');
                title.textContent = teams[team];
                section.appendChild(title);

                const teamMembersDiv = document.createElement('div');
                teamMembersDiv.className = 'team-members';

                // Separate leads and members
                let leads = data[team].filter(member => member.role.toLowerCase().includes("lead"));
                let members = data[team].filter(member => !member.role.toLowerCase().includes("lead"));

                // Combine leads and members
                let allMembers = leads.concat(members);

                allMembers.forEach(member => {
                    const memberDiv = document.createElement('div');
                    memberDiv.className = 'member';
                    memberDiv.innerHTML = `
                        <img src="${member.photo}" alt="${member.name}">
                        <div class="info">
                            <strong>${member.name}</strong>
                            <span>${member.role}</span>
                        </div>
                    `;
                    teamMembersDiv.appendChild(memberDiv);
                });

                section.appendChild(teamMembersDiv);
                teamMembersContainer.appendChild(section);
            }
        })
        .catch(error => console.error('Error loading team members:', error));
});
