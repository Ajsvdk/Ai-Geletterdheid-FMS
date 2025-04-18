import React from 'react';
import CourseCard from './CourseCard';

export default function CourseGrid({ courses }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 p-4">
      {courses.map((c) => (
        <CourseCard
          key={c.link}
          aanbieder={c.aanbieder}
          titel={c.titel}
          kosten={c.kosten}
          link={c.link}
        />
      ))}
    </div>
  );
}
