const { teams, crests } = window.OF_SIGN_IN;
const clubs = [...new Set(teams.map(team => team.club))].sort((a, b) => a.localeCompare(b, 'sv'));
const heading = document.querySelector('#login-step');
const chooser = document.querySelector('#login-clubs');
const list = document.querySelector('.login-clubs');
const search = document.querySelector('#club-search');
const back = document.querySelector('.login-back');
const form = document.querySelector('#login-form');
const teamSelect = document.querySelector('#login-team');
const empty = document.querySelector('#login-empty');

function clubMark(club) {
  const mark = document.createElement(crests[club] ? 'img' : 'span');
  mark.className = 'login-crest';
  mark.setAttribute('aria-hidden', 'true');
  if (crests[club]) {
    mark.alt = '';
    mark.src = crests[club];
    mark.loading = 'lazy';
  } else {
    mark.textContent = club.split(/\s+/).slice(0, 2).map(part => part[0]).join('');
  }
  return mark;
}

function displayClubs() {
  const query = search.value.trim().toLocaleLowerCase('sv');
  const matching = clubs.filter(club => club.toLocaleLowerCase('sv').includes(query));
  list.replaceChildren(...matching.map(club => {
    const row = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    const mark = clubMark(club);
    const name = document.createElement('strong');
    name.textContent = club;
    button.append(mark, name);
    button.addEventListener('click', () => selectClub(club));
    row.append(button);
    return row;
  }));
  empty.hidden = matching.length !== 0;
}

function selectClub(club) {
  heading.replaceChildren(clubMark(club), document.createTextNode(club));
  teamSelect.replaceChildren(new Option('Välj lag', ''));
  const groups = new Map();
  teams.filter(team => team.club === club).forEach(team => {
    const option = new Option([team.name, team.series, team.status].filter(Boolean).join(' · '), team.id);
    if (!team.group) { teamSelect.append(option); return; }
    if (!groups.has(team.group)) {
      const group = document.createElement('optgroup');
      group.label = team.group;
      groups.set(team.group, group);
      teamSelect.append(group);
    }
    groups.get(team.group).append(option);
  });
  chooser.hidden = true;
  back.hidden = false;
  form.hidden = false;
  heading.focus();
}

back.addEventListener('click', () => {
  heading.textContent = 'Välj din klubb';
  form.reset();
  form.hidden = back.hidden = true;
  chooser.hidden = false;
  search.focus();
});
search.addEventListener('input', displayClubs);
displayClubs();
