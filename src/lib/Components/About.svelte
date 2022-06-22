<script>
  import ListItem from "../UI/ListItem.svelte";
  import Profile from "../UI/Profile.svelte";
  import Paper from "../UI/Paper.svelte";

  let profileopen = false;
  let skillopen = false;

  let profiles = [
    {
      name: "Vinod Reddy",
      id: "vinod901",
      link: "https://github.com/vinod901",
      img: "profile/vinod.jpg",
      title: "Team Leader",
      description:
        "B Tech graduate, looking for a software engineer role with strong command in Rust, C, Java, Typescript, javascript, Python etc.  Excellent communication skills and ability to understand client requirements.  Continuous learner of new technologies, strategies, and tools.",
    },
    {
      name: "Shakib Shaik",
      id: "Shakib25",
      link: "https://github.com/Shakib25",
      img: "profile/shakib.jpeg",
      title: "UI Developer",
      description:
        "Enthusiastic engineering graduate with basic knowledge in coding and design. Proficient in C++, HTML 5, JavaScript, and Python. Ability to learn new softwares and technologies quickly. Capability to work in teams by providing valuable support.",
    },
    {
      name: "Fazulul Rehman",
      id: "",
      link: "",
      img: "profile/fazulul.jpeg",
      title: "Python Developer",
      description:
        " A result-oriented and self-motivated B.Tech graduate, looking for a challenging career where I can implement my coding knowledge so that further enhance my skills. Strong knowledge of HTML, CSS, Javascript, Typescript, Svelte.",
    },
    {
      name: "Saleem",
      id: "",
      link: "",
      img: "profile/saleem.jpeg",
      title: "Backend Developer",
      description:
        "An aspiring software engineer with knowledge in software engineering practices such as coding, testing, code reviews, code comments, etc.  Strong ability to communicate with clients and ability to express ideas clearly and concisely.",
    },
  ];
  let skills = [
    {
      name: "HTML",
      img: "logo/html.png",
      role: "Static Page",
      url: "https://developer.mozilla.org/en-US/docs/Web/HTML",
      description:
        "The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.",
    },
    {
      name: "CSS",
      img: "logo/css.png",
      role: "Styling",
      url: "https://developer.mozilla.org/en-US/docs/Web/CSS",
      description:
        "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.",
    },
    {
      name: "Javascript",
      img: "logo/js.png",
      role: "Frontend scripting language",
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
      description:
        "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. As of 2022, 98% of websites use JavaScript on the client side for web page behavior, often incorporating third-party libraries. ",
    },
    {
      name: "Svelte",
      img: "logo/svelte.png",
      role: "Frontend Compiler",
      url: "https://svelte.dev/",
      description:
        "Svelte is a free and open-source front end compiler. Svelte is a radical new approach to building user interfaces. Whereas traditional frameworks like React and Vue do the bulk of their work in the browser, Svelte shifts that work into a compile step that happens when you build your app.",
    },
    {
      name: "Python",
      img: "logo/python.png",
      role: "Backend scripting language",
      url: "https://www.python.org/",
      description:
        "Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.",
    },
    {
      name: "Flask",
      img: "logo/flask.png",
      role: "Backend API Framework",
      url: "https://flask.palletsprojects.com/en/2.1.x/",
      description:
        "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. ",
    },
    {
      name: "Heroku",
      img: "logo/heroku.png",
      role: "Cloud deployment service",
      url: "https://www.heroku.com/",
      description:
        "Heroku is a cloud platform as a service supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.",
    },
    {
      name: "VS Code",
      img: "logo/vscode.jpg",
      role: "IDE",
      url: "https://code.visualstudio.com/",
      description:
        "Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications",
    },
  ];
</script>

<Paper>
  <h1
    on:click={() => {
      profileopen = !profileopen;
    }}
  >
    Our Team
  </h1>
  {#if profileopen}
    <div class="grid">
      {#each profiles as profile}
        <Profile {profile} />
      {/each}
    </div>
  {/if}
</Paper>
<br /> <br />

<div class="skill">
  <Paper>
    <h1
      on:click={() => {
        skillopen = !skillopen;
      }}
    >
      Our Tech Stack
    </h1>
    {#if skillopen}
      <div class="grid">
        {#each skills as skill}
          <ListItem {skill} />
        {/each}
      </div>
    {/if}
  </Paper>
</div>

<style>
  .grid {
    display: grid;
    grid-template-columns: auto auto;
  }
  * {
    cursor: pointer;
  }
  .skill {
    background-color: aliceblue;
  }
</style>
