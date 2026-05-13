from datetime import datetime
from app import app, db, Fixture

fixtures = [

{
    'home_team': 'Mexico',
    'away_team': 'South Africa',
    'home_flag': '🇲🇽',
    'away_flag': '🇿🇦',
    'kickoff': datetime(
        2026,
        6,
        11,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'A'
},

{
    'home_team': 'Korea Republic',
    'away_team': 'Czechia',
    'home_flag': '🇰🇷',
    'away_flag': '🇨🇿',
    'kickoff': datetime(
        2026,
        6,
        12,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'A'
},

{
    'home_team': 'Canada',
    'away_team': 'Bosnia and Herzegovina',
    'home_flag': '🇨🇦',
    'away_flag': '🇧🇦',
    'kickoff': datetime(
        2026,
        6,
        12,
        19,
        00
    ),
    'stage': 'GROUP',
    'group_name': 'B'
},

{
    'home_team': 'USA',
    'away_team': 'Paraguay',
    'home_flag': '🇺🇸',
    'away_flag': '🇵🇾',
    'kickoff': datetime(
        2026,
        6,
        13,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'D'
},

{
    'home_team': 'Qatar',
    'away_team': 'Switzerland',
    'home_flag': '🇶🇦',
    'away_flag': '🇨🇭',
    'kickoff': datetime(
        2026,
        6,
        13,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'B'
},

{
    'home_team': 'Brazil',
    'away_team': 'Morocco',
    'home_flag': '🇧🇷',
    'away_flag': '🇲🇦',
    'kickoff': datetime(
        2026,
        6,
        13,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'C'
},

{
    'home_team': 'Haiti',
    'away_team': 'Scotland',
    'home_flag': '🇭🇹',
    'away_flag': '🏴󠁧󠁢󠁳󠁣󠁴󠁿',
    'kickoff': datetime(
        2026,
        6,
        14,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'C'
},

{
    'home_team': 'Australia',
    'away_team': 'Turkey',
    'home_flag': '🇦🇺',
    'away_flag': '🇹🇷',
    'kickoff': datetime(
        2026,
        6,
        14,
        4,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'D'
},
{
    'home_team': 'Germany',
    'away_team': 'Curaçao',
    'home_flag': '🇩🇪',
    'away_flag': '🇨🇼',
    'kickoff': datetime(
        2026,
        6,
        14,
        17,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'E'
},

{
    'home_team': 'Netherlands',
    'away_team': 'Japan',
    'home_flag': '🇳🇱',
    'away_flag': '🇯🇵',
    'kickoff': datetime(
        2026,
        6,
        14,
        20,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'F'
},

{
    'home_team': "Ivory Coast",
    'away_team': 'Ecuador',
    'home_flag': '🇨🇮',
    'away_flag': '🇪🇨',
    'kickoff': datetime(
        2026,
        6,
        14,
        23,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'E'
},

{
    'home_team': 'Sweden',
    'away_team': 'Tunisia',
    'home_flag': '🇸🇪',
    'away_flag': '🇹🇳',
    'kickoff': datetime(
        2026,
        6,
        15,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'F'
},

{
    'home_team': 'Spain',
    'away_team': 'Cape Verde',
    'home_flag': '🇪🇸',
    'away_flag': '🇨🇻',
    'kickoff': datetime(
        2026,
        6,
        15,
        16,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'H'
},

{
    'home_team': 'Belgium',
    'away_team': 'Egypt',
    'home_flag': '🇧🇪',
    'away_flag': '🇪🇬',
    'kickoff': datetime(
        2026,
        6,
        15,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'G'
},

{
    'home_team': 'Saudi Arabia',
    'away_team': 'Uruguay',
    'home_flag': '🇸🇦',
    'away_flag': '🇺🇾',
    'kickoff': datetime(
        2026,
        6,
        15,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'H'
},

{
    'home_team': 'Iran',
    'away_team': 'New Zealand',
    'home_flag': '🇮🇷',
    'away_flag': '🇳🇿',
    'kickoff': datetime(
        2026,
        6,
        16,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'G'
},

{
    'home_team': 'France',
    'away_team': 'Senegal',
    'home_flag': '🇫🇷',
    'away_flag': '🇸🇳',
    'kickoff': datetime(
        2026,
        6,
        16,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'I'
},

{
    'home_team': 'Iraq',
    'away_team': 'Norway',
    'home_flag': '🇮🇶',
    'away_flag': '🇳🇴',
    'kickoff': datetime(
        2026,
        6,
        16,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'I'
},

{
    'home_team': 'Argentina',
    'away_team': 'Algeria',
    'home_flag': '🇦🇷',
    'away_flag': '🇩🇿',
    'kickoff': datetime(
        2026,
        6,
        17,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'J'
},

{
    'home_team': 'Austria',
    'away_team': 'Jordan',
    'home_flag': '🇦🇹',
    'away_flag': '🇯🇴',
    'kickoff': datetime(
        2026,
        6,
        17,
        4,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'J'
},

{
    'home_team': 'Portugal',
    'away_team': 'DR Congo',
    'home_flag': '🇵🇹',
    'away_flag': '🇨🇩',
    'kickoff': datetime(
        2026,
        6,
        17,
        17,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'K'
},

{
    'home_team': 'England',
    'away_team': 'Croatia',
    'home_flag': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    'away_flag': '🇭🇷',
    'kickoff': datetime(
        2026,
        6,
        17,
        20,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'L'
},

{
    'home_team': 'Ghana',
    'away_team': 'Panama',
    'home_flag': '🇬🇭',
    'away_flag': '🇵🇦',
    'kickoff': datetime(
        2026,
        6,
        17,
        23,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'L'
},

{
    'home_team': 'Uzbekistan',
    'away_team': 'Colombia',
    'home_flag': '🇺🇿',
    'away_flag': '🇨🇴',
    'kickoff': datetime(
        2026,
        6,
        18,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'K'
},
{
    'home_team': 'Czechia',
    'away_team': 'South Africa',
    'home_flag': '🇨🇿',
    'away_flag': '🇿🇦',
    'kickoff': datetime(
        2026,
        6,
        18,
        16,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'A'
},

{
    'home_team': 'Switzerland',
    'away_team': 'Bosnia and Herzegovina',
    'home_flag': '🇨🇭',
    'away_flag': '🇧🇦',
    'kickoff': datetime(
        2026,
        6,
        18,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'B'
},

{
    'home_team': 'Canada',
    'away_team': 'Qatar',
    'home_flag': '🇨🇦',
    'away_flag': '🇶🇦',
    'kickoff': datetime(
        2026,
        6,
        18,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'B'
},

{
    'home_team': 'Mexico',
    'away_team': 'Korea Republic',
    'home_flag': '🇲🇽',
    'away_flag': '🇰🇷',
    'kickoff': datetime(
        2026,
        6,
        19,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'A'
},

{
    'home_team': 'USA',
    'away_team': 'Australia',
    'home_flag': '🇺🇸',
    'away_flag': '🇦🇺',
    'kickoff': datetime(
        2026,
        6,
        19,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'D'
},

{
    'home_team': 'Scotland',
    'away_team': 'Morocco',
    'home_flag': '🏴󠁧󠁢󠁳󠁣󠁴󠁿',
    'away_flag': '🇲🇦',
    'kickoff': datetime(
        2026,
        6,
        19,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'C'
},

{
    'home_team': 'Brazil',
    'away_team': 'Haiti',
    'home_flag': '🇧🇷',
    'away_flag': '🇭🇹',
    'kickoff': datetime(
        2026,
        6,
        20,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'C'
},

{
    'home_team': 'Turkey',
    'away_team': 'Paraguay',
    'home_flag': '🇹🇷',
    'away_flag': '🇵🇾',
    'kickoff': datetime(
        2026,
        6,
        20,
        4,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'D'
},

{
    'home_team': 'Netherlands',
    'away_team': 'Sweden',
    'home_flag': '🇳🇱',
    'away_flag': '🇸🇪',
    'kickoff': datetime(
        2026,
        6,
        20,
        17,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'F'
},

{
    'home_team': 'Germany',
    'away_team': "Ivory Coast",
    'home_flag': '🇩🇪',
    'away_flag': '🇨🇮',
    'kickoff': datetime(
        2026,
        6,
        20,
        20,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'E'
},

{
    'home_team': 'Ecuador',
    'away_team': 'Curaçao',
    'home_flag': '🇪🇨',
    'away_flag': '🇨🇼',
    'kickoff': datetime(
        2026,
        6,
        21,
        0,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'E'
},

{
    'home_team': 'Tunisia',
    'away_team': 'Japan',
    'home_flag': '🇹🇳',
    'away_flag': '🇯🇵',
    'kickoff': datetime(
        2026,
        6,
        21,
        4,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'F'
},

{
    'home_team': 'Spain',
    'away_team': 'Saudi Arabia',
    'home_flag': '🇪🇸',
    'away_flag': '🇸🇦',
    'kickoff': datetime(
        2026,
        6,
        21,
        16,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'H'
},

{
    'home_team': 'Belgium',
    'away_team': 'Iran',
    'home_flag': '🇧🇪',
    'away_flag': '🇮🇷',
    'kickoff': datetime(
        2026,
        6,
        21,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'G'
},

{
    'home_team': 'Uruguay',
    'away_team': 'Cape Verde',
    'home_flag': '🇺🇾',
    'away_flag': '🇨🇻',
    'kickoff': datetime(
        2026,
        6,
        21,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'H'
},

{
    'home_team': 'New Zealand',
    'away_team': 'Egypt',
    'home_flag': '🇳🇿',
    'away_flag': '🇪🇬',
    'kickoff': datetime(
        2026,
        6,
        22,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'G'
},
{
    'home_team': 'Argentina',
    'away_team': 'Austria',
    'home_flag': '🇦🇷',
    'away_flag': '🇦🇹',
    'kickoff': datetime(
        2026,
        6,
        22,
        17,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'J'
},

{
    'home_team': 'France',
    'away_team': 'Iraq',
    'home_flag': '🇫🇷',
    'away_flag': '🇮🇶',
    'kickoff': datetime(
        2026,
        6,
        22,
        21,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'I'
},

{
    'home_team': 'Norway',
    'away_team': 'Senegal',
    'home_flag': '🇳🇴',
    'away_flag': '🇸🇳',
    'kickoff': datetime(
        2026,
        6,
        23,
        0,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'I'
},

{
    'home_team': 'Jordan',
    'away_team': 'Algeria',
    'home_flag': '🇯🇴',
    'away_flag': '🇩🇿',
    'kickoff': datetime(
        2026,
        6,
        23,
        3,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'J'
},

{
    'home_team': 'Portugal',
    'away_team': 'Uzbekistan',
    'home_flag': '🇵🇹',
    'away_flag': '🇺🇿',
    'kickoff': datetime(
        2026,
        6,
        23,
        17,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'K'
},

{
    'home_team': 'England',
    'away_team': 'Ghana',
    'home_flag': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    'away_flag': '🇬🇭',
    'kickoff': datetime(
        2026,
        6,
        23,
        20,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'L'
},

{
    'home_team': 'Panama',
    'away_team': 'Croatia',
    'home_flag': '🇵🇦',
    'away_flag': '🇭🇷',
    'kickoff': datetime(
        2026,
        6,
        23,
        23,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'L'
},

{
    'home_team': 'Colombia',
    'away_team': 'DR Congo',
    'home_flag': '🇨🇴',
    'away_flag': '🇨🇩',
    'kickoff': datetime(
        2026,
        6,
        24,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'K'
},

{
    'home_team': 'Switzerland',
    'away_team': 'Canada',
    'home_flag': '🇨🇭',
    'away_flag': '🇨🇦',
    'kickoff': datetime(
        2026,
        6,
        24,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'B'
},

{
    'home_team': 'Bosnia and Herzegovina',
    'away_team': 'Qatar',
    'home_flag': '🇧🇦',
    'away_flag': '🇶🇦',
    'kickoff': datetime(
        2026,
        6,
        24,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'B'
},

{
    'home_team': 'Scotland',
    'away_team': 'Brazil',
    'home_flag': '🏴󠁧󠁢󠁳󠁣󠁴󠁿',
    'away_flag': '🇧🇷',
    'kickoff': datetime(
        2026,
        6,
        24,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'C'
},

{
    'home_team': 'Morocco',
    'away_team': 'Haiti',
    'home_flag': '🇲🇦',
    'away_flag': '🇭🇹',
    'kickoff': datetime(
        2026,
        6,
        24,
        22,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'C'
},

{
    'home_team': 'Czechia',
    'away_team': 'Mexico',
    'home_flag': '🇨🇿',
    'away_flag': '🇲🇽',
    'kickoff': datetime(
        2026,
        6,
        25,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'A'
},

{
    'home_team': 'South Africa',
    'away_team': 'Korea Republic',
    'home_flag': '🇿🇦',
    'away_flag': '🇰🇷',
    'kickoff': datetime(
        2026,
        6,
        25,
        1,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'A'
},

{
    'home_team': 'Curaçao',
    'away_team': "Ivory Coast",
    'home_flag': '🇨🇼',
    'away_flag': '🇨🇮',
    'kickoff': datetime(
        2026,
        6,
        25,
        20,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'E'
},

{
    'home_team': 'Ecuador',
    'away_team': 'Germany',
    'home_flag': '🇪🇨',
    'away_flag': '🇩🇪',
    'kickoff': datetime(
        2026,
        6,
        25,
        20,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'E'
},{
    'home_team': 'Japan',
    'away_team': 'Sweden',
    'home_flag': '🇯🇵',
    'away_flag': '🇸🇪',
    'kickoff': datetime(
        2026,
        6,
        25,
        23,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'F'
},

{
    'home_team': 'Tunisia',
    'away_team': 'Netherlands',
    'home_flag': '🇹🇳',
    'away_flag': '🇳🇱',
    'kickoff': datetime(
        2026,
        6,
        25,
        23,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'F'
},

{
    'home_team': 'Turkey',
    'away_team': 'USA',
    'home_flag': '🇹🇷',
    'away_flag': '🇺🇸',
    'kickoff': datetime(
        2026,
        6,
        26,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'D'
},

{
    'home_team': 'Paraguay',
    'away_team': 'Australia',
    'home_flag': '🇵🇾',
    'away_flag': '🇦🇺',
    'kickoff': datetime(
        2026,
        6,
        26,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'D'
},

{
    'home_team': 'Norway',
    'away_team': 'France',
    'home_flag': '🇳🇴',
    'away_flag': '🇫🇷',
    'kickoff': datetime(
        2026,
        6,
        26,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'I'
},

{
    'home_team': 'Senegal',
    'away_team': 'Iraq',
    'home_flag': '🇸🇳',
    'away_flag': '🇮🇶',
    'kickoff': datetime(
        2026,
        6,
        26,
        19,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'I'
},

{
    'home_team': 'Cape Verde',
    'away_team': 'Saudi Arabia',
    'home_flag': '🇨🇻',
    'away_flag': '🇸🇦',
    'kickoff': datetime(
        2026,
        6,
        27,
        0,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'H'
},

{
    'home_team': 'Uruguay',
    'away_team': 'Spain',
    'home_flag': '🇺🇾',
    'away_flag': '🇪🇸',
    'kickoff': datetime(
        2026,
        6,
        27,
        0,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'H'
},

{
    'home_team': 'Egypt',
    'away_team': 'Iran',
    'home_flag': '🇪🇬',
    'away_flag': '🇮🇷',
    'kickoff': datetime(
        2026,
        6,
        27,
        3,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'G'
},

{
    'home_team': 'New Zealand',
    'away_team': 'Belgium',
    'home_flag': '🇳🇿',
    'away_flag': '🇧🇪',
    'kickoff': datetime(
        2026,
        6,
        27,
        3,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'G'
},

{
    'home_team': 'Panama',
    'away_team': 'England',
    'home_flag': '🇵🇦',
    'away_flag': '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    'kickoff': datetime(
        2026,
        6,
        27,
        21,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'L'
},

{
    'home_team': 'Croatia',
    'away_team': 'Ghana',
    'home_flag': '🇭🇷',
    'away_flag': '🇬🇭',
    'kickoff': datetime(
        2026,
        6,
        27,
        21,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'L'
},

{
    'home_team': 'Colombia',
    'away_team': 'Portugal',
    'home_flag': '🇨🇴',
    'away_flag': '🇵🇹',
    'kickoff': datetime(
        2026,
        6,
        27,
        23,
        30
    ),
    'stage': 'GROUP',
    'group_name': 'K'
},

{
    'home_team': 'DR Congo',
    'away_team': 'Uzbekistan',
    'home_flag': '🇨🇩',
    'away_flag': '🇺🇿',
    'kickoff': datetime(
        2026,
        6,
        27,
        23,
        30
    ),
    'stage': 'GROUP',
    'group_name': 'K'
},

{
    'home_team': 'Algeria',
    'away_team': 'Austria',
    'home_flag': '🇩🇿',
    'away_flag': '🇦🇹',
    'kickoff': datetime(
        2026,
        6,
        28,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'J'
},

{
    'home_team': 'Jordan',
    'away_team': 'Argentina',
    'home_flag': '🇯🇴',
    'away_flag': '🇦🇷',
    'kickoff': datetime(
        2026,
        6,
        28,
        2,
        0
    ),
    'stage': 'GROUP',
    'group_name': 'J'
},
{
    'home_team': '2A',
    'away_team': '2B',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        6,
        28,
        19,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1C',
    'away_team': '2F',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        6,
        29,
        17,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1E',
    'away_team': '3ABCDF',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        6,
        29,
        20,
        30
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1F',
    'away_team': '2C',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        6,
        30,
        1,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '2E',
    'away_team': '2I',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        6,
        30,
        17,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1I',
    'away_team': '3CDFGH',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        6,
        30,
        21,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1A',
    'away_team': '3CEFHI',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        1,
        1,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1L',
    'away_team': '3EHIJK',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        1,
        16,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1G',
    'away_team': '3AEHIJ',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        1,
        20,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1D',
    'away_team': '3BEFIJ',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        2,
        0,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1H',
    'away_team': '2J',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        2,
        19,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '2K',
    'away_team': '2L',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        2,
        23,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1B',
    'away_team': '3EFGIJ',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        3,
        3,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '2D',
    'away_team': '2G',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        3,
        18,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1J',
    'away_team': '2H',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        3,
        22,
        0
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},

{
    'home_team': '1K',
    'away_team': '3DEIJL',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        4,
        1,
        30
    ),
    'stage': 'ROUND_OF_32',
    'group_name': None
},{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        4,
        17,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        4,
        21,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        5,
        20,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        6,
        0,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        6,
        19,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        7,
        0,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        7,
        16,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        7,
        20,
        0
    ),
    'stage': 'ROUND_OF_16',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        9,
        20,
        0
    ),
    'stage': 'QUARTER_FINAL',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        10,
        19,
        0
    ),
    'stage': 'QUARTER_FINAL',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        11,
        21,
        0
    ),
    'stage': 'QUARTER_FINAL',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        12,
        1,
        0
    ),
    'stage': 'QUARTER_FINAL',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        14,
        19,
        0
    ),
    'stage': 'SEMI_FINAL',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        15,
        19,
        0
    ),
    'stage': 'SEMI_FINAL',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        18,
        21,
        0
    ),
    'stage': 'THIRD_PLACE',
    'group_name': None
},

{
    'home_team': 'TBC',
    'away_team': 'TBC',
    'home_flag': '',
    'away_flag': '',
    'kickoff': datetime(
        2026,
        7,
        19,
        19,
        0
    ),
    'stage': 'FINAL',
    'group_name': None
}

]

with app.app_context():

    for fixture_data in fixtures:

        existing_fixture = Fixture.query.filter_by(

    home_team=fixture_data['home_team'],
    away_team=fixture_data['away_team'],
    kickoff=fixture_data['kickoff']

        ).first()

        if not existing_fixture:

            fixture = Fixture(

                home_team=fixture_data['home_team'],

                away_team=fixture_data['away_team'],

                home_flag=fixture_data['home_flag'],

                away_flag=fixture_data['away_flag'],

                kickoff=fixture_data['kickoff'],

                stage=fixture_data['stage'],

                group_name=fixture_data['group_name']
            )

            db.session.add(fixture)

    db.session.commit()

    print('Fixtures loaded successfully!')