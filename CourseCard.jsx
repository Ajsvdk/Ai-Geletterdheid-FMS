import React from 'react';

export default function CourseCard({ aanbieder, titel, kosten, link }) {
  return (
    <div className="card p-4 shadow-lg rounded-lg">
      <h3 className="text-xl font-bold">{titel}</h3>
      <p className="text-gray-600">{aanbieder}</p>
      <p className="mt-2 font-semibold">{kosten}</p>
      <a
        href={link}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-4 inline-block px-4 py-2 bg-blue-500 text-white rounded"
      >
        Bekijk cursus
      </a>
    </div>
  );
}
