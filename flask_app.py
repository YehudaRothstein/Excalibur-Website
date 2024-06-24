<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link href="https://db.onlinewebfonts.com/c/a9ca19a608d18285fbd70cb40818bb79?family=Copperplate+W02+Bold" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/mainpage.css') }}">
</head>
<body>
<header>
    <nav>
        <div class="nav-left">
            <a href="/home">Excalibur FRC 6738</a>
        </div>
        <button class="menu-toggle" aria-label="Open menu">&#9776;</button>
        <ul class="nav-links">
            <li><a href="#hero">Home</a></li>
            <li><a href="#team">Team</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#schedule">Schedule</a></li>
            <li><a href="#contacts">Contacts</a></li>
            <li><a href="#" role="button">Donate</a></li>
        </ul>
        <div class="profile-section">
            <img src="{{ url_for('static', filename='profiles/' + current_user.profile_picture) }}" alt="Profile Picture" class="profile-pic-large">
            <div class="profile-dropdown">
                <a href="{{ url_for('profile') }}">View Profile</a>
                <a href="#settings">Settings</a>
                <a href="{{ url_for('logout') }}">Logout</a>
            </div>
        </div>
    </nav>
</header>
    <section id="hero" class="hero">
        <div class="hero-content">
            <h1>Welcome to Excalibur!, {{ full_name }}</h1>
            <p>Innovating the future with robotics and technology.</p>
            <br>
            <a href="{{ url_for('scout') }}" class="btn">Scout Now</a>
        </div>
    </section>
    <main class="container">
        <section id="dashboard">
            <h2>Dashboard</h2>
            <div class="grid">
                <div class="card">
                    <img src="https://excaliburfrc.github.io/resources/Logo.png" alt="Teams">
                    <div class="card-content">
                        <h3>Teams</h3>
                        <p>View all team members and their roles.</p>
                        <button class="view-teams-btn" onclick="viewTeams()">View Members</button>
                    </div>
                </div>
                <div class="card">
                    <img src="static/img/logo_resources.png" alt="Sponsors">
                    <div class="card-content">
                        <h3>Sponsors</h3>
                        <p>Check out our sponsors for this season!</p>
                        <button class="view-teams-btn" onclick="viewSponsors()">View Sponsors</button>
                    </div>
                </div>
                <div class="card">
                    <img src="static/img/logo_statistics.png" alt="Statistics">
                    <div class="card-content">
                        <h3>Statistics</h3>
                        <p>View team performance statistics.</p>
                        <button class="view-teams-btn" onclick="viewStats()">View Stats</button>
                    </div>
                </div>
                <div class="card">
                    <img src="static/img/logo_resources.png" alt="Resources">
                    <div class="card-content">
                        <h3>Resources</h3>
                        <p>Access training and resources.</p>
                        <button class="view-teams-btn" onclick="viewResources()">View Resources</button>
                    </div>
                </div>
            </div>
        </section>
        <section id="team" class="side-content-image">
            <div class="content">
                <h2>Team Overview</h2>
                <p>Our team consists of passionate individuals who are dedicated to innovation and excellence. Meet the members who make our success possible.</p>
            </div>
            <div class="image">
                <img src="static/img/excalibur_team_photo.JPG" alt="Team photo">
            </div>
        </section>
        <section id="projects" class="side-content-image">
            <div class="content">
                <h2>Projects</h2>
                <p>We are constantly working on exciting projects that push the boundaries of technology and innovation. Explore our current and past projects.</p>
            </div>
            <div class="image">
                <img src="static/img/prizes.JPG" alt="Project photo">
            </div>
        </section>
        <section id="schedule" class="side-content-image">
            <div class="content">
                <h2>Schedule</h2>
                <p>Stay up-to-date with our latest events and activities. Check out our schedule to see what's coming up next.</p>
            </div>
            <div class="image">
                <img src="static/img/team2024.JPG" alt="Schedule photo">
            </div>
        </section>
        <section id="contacts" class="side-content-image">
            <div class="content">
                <h2>Contact Information</h2>
                <p>We'd love to hear from you! Whether you have a question or just want to say hello, feel free to get in touch with us.</p>
            </div>
            <div class="image">
                <img src="static/img/con.JPG" alt="Contact photo">
            </div>
        </section>
    </main>
    <section aria-label="Subscribe example" class="subscribe-section">
        <div class="container">
            <article>
                <h2>Subscribe to our newsletter</h2>
                <p>Stay updated with our latest news</p>
                <form id="subscribeForm">
                    <input type="text" id="firstname" name="firstname" placeholder="First Name" aria-label="First Name" required>
                    <input type="email" id="email" name="email" placeholder="Email Address" aria-label="Email Address" required>
                    <button id="sub_btton" type="submit">Subscribe</button>
                </form>
            </article>
        </div>
    </section>
    <footer>
        <small><a href="#">Privacy Policy</a> • <a href="#">Terms of Service</a></small>
        <p>&copy; 2024 Excalibur FRC 6738</p>
    </footer>
    <script>
        function viewTeams() {
            window.location.href = "{{ url_for('contacts') }}";
        }

        function viewSponsors() {
            window.location.href = "{{ url_for('sponsors') }}";
        }

        function viewStats() {
            alert('Viewing stats...');
        }

        function viewResources() {
            alert('Viewing resources...');
        }

        document.querySelector('.menu-toggle').addEventListener('click', function() {
            document.querySelector('.nav-links').classList.toggle('active');
        });
    </script>
</body>
</html>
